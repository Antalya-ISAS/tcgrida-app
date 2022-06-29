# -*- coding: UTF-8 -*-
################################

## Formatting.

import sqlite3
import sys, os
import platform
import cv2
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QPropertyAnimation, QMetaObject, QSize, Qt, QTimer
from PyQt6.QtWidgets import *

# from PyQt6.QtWidgets import QShortcut


# GUI FILE
from app_modules import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("System: " + platform.system())
        print("Version: " + platform.release())
        self.desktop = QtGui.QGuiApplication.primaryScreen()
        # cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        self.screenRect = self.desktop.availableGeometry()
        self.screen_h = self.screenRect.height()
        self.screen_w = self.screenRect.width()

        self.dir = ""  # Used to store PATH
        self.vid_value = 0  # Used to check the recording

        ## INITIALIZE CAMGEAR
        self.ui.page_home.vc = cv2.VideoCapture(0)

        ## CONNECT TO THE DATABASE
        self.database = sqlite3.connect("settings.db")
        self.cursor = self.database.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS settings (path TEXT, appearance INT, camera INT)"
        )

        # SQL Path
        self.cursor.execute("SELECT path FROM settings")
        path_list = self.cursor.fetchall()
        self.cursor.execute("SELECT appearance FROM settings")
        appearance_list = self.cursor.fetchall()
        self.cursor.execute("SELECT camera FROM settings")
        camera_list = self.cursor.fetchall()

        if len(path_list) == 0 or len(appearance_list) == 0 or len(camera_list) == 0:
            self.cursor.execute("DELETE FROM settings")
            self.cursor.execute(
                "INSERT INTO settings (path, appearance, camera) Values(?,?,?)",
                ("", 0, 0),
            )
            self.camera_state = 0
            self.database.commit()

        else:
            for column in path_list:
                for item in column:
                    self.dir = str(item)
                    self.ui.lineEditSettings.setText(self.dir)
            for column in appearance_list:
                for item in column:
                    if item == 1:
                        self.ui.toggle.setChecked(True)
                    elif item == 0:
                        self.ui.toggle.setChecked(False)
            UIFunctions.change_mode(self)
            for column in camera_list:
                for item in column:
                    if item == 0:
                        self.ui.comboBox.setCurrentIndex(0)
                        self.camera_state = 0
                    elif item == 1:
                        self.ui.comboBox.setCurrentIndex(1)
                        self.camera_state = 1
                    elif item == 2:
                        self.ui.comboBox.setCurrentIndex(2)
                        self.camera_state = 2

        ## START TIMER (TO UPDATE FRAMES)
        self.ui.page_home.timer = QTimer()
        self.ui.page_home.timer.timeout.connect(lambda: UIFunctions.nextFrameSlot(self))

        ## START TIMER (WEBCAM CHANGE)
        self.timer = QTimer()

        ## START CAPTURING CAMERA VIEW
        UIFunctions.openCam(self, self.camera_state)
        print(self.ui.comboBox.currentText())
        self.ui.comboBox.currentIndexChanged.connect(
            lambda: UIFunctions.openCam(self, int(self.ui.comboBox.currentText()[-1]))
        )
        print(self.ui.comboBox.currentText())

        ###################################################
        ## WINDOW ATTRIBUTES
        ###################################################

        ## REMOVE STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        ## SET THE WINDOW TITLE
        self.setWindowTitle("tcGrida App")
        UIFunctions.labelTitle(self, "tcGrida App")
        UIFunctions.labelDescription(self, "Your underwater henchman.")

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        # self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)

        ## TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True)
        )

        ## ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(
            self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True
        )
        UIFunctions.addNewMenu(
            self,
            "INFO PAGE",
            "btn_info",
            "url(:/16x16/icons/16x16/cil-align-center.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "SETTINGS",
            "btn_settings",
            "url(:/16x16/icons/16x16/cil-settings.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "FOLLOW US!",
            "btn_links",
            "url(:/16x16/icons/16x16/cil-thumb-up.png)",
            False,
        )

        ## SELECT START MENU
        UIFunctions.selectStandardMenu(self, "btn_home")

        ## SELECT START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        ## CONNECT SNAPSHOT BUTTON
        self.ui.photo_button.clicked.connect(lambda: UIFunctions.take_photo(self))

        ## CONNECT RECORDING BUTTON
        self.ui.video_button.clicked.connect(lambda: UIFunctions.record_video(self))

        ## CONNECT FULL SCREEN BUTTON
        self.ui.btn_fullscreen.clicked.connect(lambda: UIFunctions.full_screen(self))
        # self.shortcut = QShortcut("F", self)
        # self.shortcut.activated.connect(lambda: UIFunctions.full_screen(self))

        ## CONNECT TOGGLE BUTTON
        self.ui.toggle.stateChanged.connect(lambda: UIFunctions.change_mode(self))

        ## CONNECT LINK BUTTONS
        self.ui.instaLinkButton.clicked.connect(
            lambda: UIFunctions.open_link("https://www.instagram.com/antalya.isas/")
        )
        self.ui.gitLinkButton.clicked.connect(
            lambda: UIFunctions.open_link("https://github.com/Antalya-ISAS")
        )
        self.ui.webLinkButton.clicked.connect(
            lambda: UIFunctions.open_link("https://antalyaisas.com/")
        )
        self.ui.formLinkButton.clicked.connect(
            lambda: UIFunctions.open_link("https://airtable.com/shrD4gdRqPPUZeYjH")
        )
        self.ui.youtubeLinkButton.clicked.connect(
            lambda: UIFunctions.open_link(
                "https://www.youtube.com/channel/UCWZvgA6EhvlmvoRbStbpwaQ/featured"
            )
        )

        ## CONNECT FOLDER BUTTON
        self.ui.pushButtonSettings.clicked.connect(
            lambda: UIFunctions.openDirWindow(self)
        )

        ## WINDOWS ==> MOVE / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                # if (
                #     self.dragPos.y() == 0
                #     or self.dragPos.x() == 0
                #     or self.dragPos.y() == self.screen_h - 1
                #     or self.dragPos.x() == self.screen_w - 1
                # ):
                #     UIFunctions.maximize_restore(self)

                event.accept()

        ## WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        ## LOAD DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ###################################################
        ## END - WINDOW ATTRIBUTES
        ###################################################

        ## SHOW ==> MAIN WINDOW
        self.showMaximized()

    ###################################################
    ## DYNAMIC MENUS - FUNCTIONS
    ###################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE INFO
        if btnWidget.objectName() == "btn_info":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_info)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "INFO PAGE")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE SETTINGS
        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            UIFunctions.resetStyle(self, "btn_settings")
            UIFunctions.labelPage(self, "SETTINGS")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE LINKS
        if btnWidget.objectName() == "btn_links":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_links)
            UIFunctions.resetStyle(self, "btn_links")
            UIFunctions.labelPage(self, "FOLLOW US!")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def mousePressEvent(self, event):
        self.dragPos = event.position()

    ###################################################
    ## END -> DYNAMIC MENUS - FUNCTIONS
    ###################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont("fonts/segoeui.ttf")
    QtGui.QFontDatabase.addApplicationFont("fonts/segoeuib.ttf")

    window = MainWindow()
    sys.exit(app.exec())
