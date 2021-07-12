################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################
import sqlite3
import sys, time, os
import platform
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import (QCoreApplication, QFile, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTextStream, QTime, QUrl, Qt, QEvent, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from app_modules import *

## LINK TEMPLATE FOR THE "FOLLOW US" PAGE
linkTemplate = '<a href={0}>{1}</a>'

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.environment = os.environ["HOMEPATH"]
        self.deger=0
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        # self.num_photos = 0 # this will be used to count the num of photos
        self.dir = "" # this will be used to store paths

        ## CONNECT TO THE DATABASE
        self.database = sqlite3.connect("settings.db")
        self.cursor = self.database.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS settings_path (path TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS settings_appearance(appearance INT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS settings_camera (camera INT)")

        #SQL Path
        self.cursor.execute("SELECT * FROM settings_path")
        liste = self.cursor.fetchall()

        if(len(liste)==0):
            self.cursor.execute("INSERT INTO settings_path Values(?)",("",))
            self.database.commit()

        else:
            for column in liste:
                for item in column:
                    self.dir = str(item)
                    self.ui.lineEditSettings.setText(self.dir)
        #SQL Appearance
        self.cursor.execute("SELECT * FROM settings_appearance")
        liste = self.cursor.fetchall()
        if(len(liste)==0):
            self.cursor.execute("INSERT INTO settings_appearance Values(?)",(0,))
            self.database.commit()

        
        else:
            for column in liste:
                for item in column:
                    if item == 1:
                        self.ui.toggle.setChecked(True)
                    elif item == 0:
                        self.ui.toggle.setChecked(False)
            UIFunctions.change_mode(self)

        #SQL Camera
        self.cursor.execute("SELECT * FROM settings_camera")
        liste = self.cursor.fetchall() 
        if(len(liste)==0):
            self.cursor.execute("INSERT INTO settings_camera Values(?)",(0,))
            self.camera_state=0
            self.database.commit()

        
        else:
            for column in liste:
                for item in column:
                    if item == 0:
                        self.ui.comboBox.setCurrentIndex(0)
                        self.camera_state=0
                    elif item == 1:
                        self.ui.comboBox.setCurrentIndex(1)
                        self.camera_state=1
                    elif item == 2:
                        self.ui.comboBox.setCurrentIndex(2)
                        self.camera_state=2
        ## START TIMER (TO UPDATE FRAMES)
        self.ui.page_home.timer = QTimer()
        self.ui.page_home.timer.timeout.connect(self.nextFrameSlot)

        ## START TIMER (WEBCAM CHANGE)
        self.timer = QTimer()

        ## START CAPTURING CAMERA VIEW
        self.openCam(self.camera_state)
        print(self.ui.comboBox.currentText())
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.openCam(int(self.ui.comboBox.currentText()[-1])))
        print(self.ui.comboBox.currentText())

        ###################################################
        ## WINDOW ATTRIBUTES
        ###################################################

        ## REMOVE STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        ## SET THE WINDOW TITLE
        self.setWindowTitle('tcGrida App')
        UIFunctions.labelTitle(self, 'tcGrida App')
        UIFunctions.labelDescription(self, 'Your underwater henchman.')

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        #self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)

        ## TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        ## ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "INFO PAGE", "btn_info", "url(:/16x16/icons/16x16/cil-align-center.png)", True)
        UIFunctions.addNewMenu(self, "SETTINGS", "btn_settings", "url(:/16x16/icons/16x16/cil-settings.png)", True)
        UIFunctions.addNewMenu(self, "FOLLOW US!", "btn_links", "url(:/16x16/icons/16x16/cil-thumb-up.png)", False)

        ## SELECT START MENU
        UIFunctions.selectStandardMenu(self, "btn_home")

        ## SELECT START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        ## CONNECT SNAPSHOT BUTTON
        self.ui.photo_button.clicked.connect(lambda: UIFunctions.take_photo(self))

        ## CONNECT RECORDING BUTTON
        self.ui.video_button.clicked.connect(lambda: UIFunctions.shot_video(self))
       

        ## CONNECT TOGGLE BUTTON
        self.ui.toggle.stateChanged.connect(lambda: UIFunctions.change_mode(self))

        ## CONNECT LINK BUTTONS
        self.ui.instaLinkButton.clicked.connect(lambda: UIFunctions.open_link("https://www.instagram.com/antalya.isas/"))
        self.ui.gitLinkButton.clicked.connect(lambda: UIFunctions.open_link("https://github.com/Antalya-ISAS"))
        self.ui.webLinkButton.clicked.connect(lambda: UIFunctions.open_link("https://antalyaisas.com/"))
        self.ui.formLinkButton.clicked.connect(lambda: UIFunctions.open_link("https://airtable.com/shrD4gdRqPPUZeYjH"))
        self.ui.youtubeLinkButton.clicked.connect(lambda: UIFunctions.open_link("https://www.youtube.com/channel/UCWZvgA6EhvlmvoRbStbpwaQ/featured"))

        ## CONNECT FOLDER BUTTON
        self.ui.pushButtonSettings.clicked.connect(lambda: UIFunctions.openDirWindow(self))

        ## WINDOWS ==> MOVE / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                try:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
                except:
                    pass

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

    # OPEN CAMERA
    def openCam(self, cam):
        self.cursor.execute("SELECT * FROM settings_camera")
        liste = self.cursor.fetchall()

        for item in liste:
            for i in item:
                old_camera=i
        self.cursor.execute("UPDATE settings_camera set camera = ? where camera = ?",(self.ui.comboBox.currentIndex(),old_camera))
        self.database.commit()        
        self.ui.page_home.vc = cv2.VideoCapture(cam,cv2.CAP_DSHOW)
        # vc.set(5, 30)  #set FPS
        self.ui.page_home.vc.set(3, self.ui.page_home.width()*2)  # set width
        self.ui.page_home.vc.set(4, self.ui.page_home.height()*2)  # set height
        self.ui.page_home.timer.start(round(1000. / 24))
        

    # https://stackoverflow.com/questions/41103148/capture-webcam-video-using-pyqt
    def nextFrameSlot(self):
        try:
            rval, frame = self.ui.page_home.vc.read()
            #TODO: Buraya bir kontrol mekanizması getirilmeli ve frame boş ise boş olmayana kadar beklenmeli
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #resize = cv2.cv2.resize(frame, (self.ui.page_home.width()*2, self.ui.page_home.height()*2))
            #image = QImage(resize, resize.shape[1], resize.shape[0], QImage.Format_RGB888)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.ui.page_home.label.setPixmap(pixmap)
        # logo_pixmap = cv2.cv2.imread('logo.png')
        # dst = cv2.addWeighted(frame,1.0,logo_pixmap,0.7,0) #bu satır düzeltilecek
        except:
            self.ui.page_home.label.setText("Could not open %s"%self.ui.comboBox.currentText())

        

    ###################################################
    ## END -> DYNAMIC MENUS - FUNCTIONS
    ###################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')

    window = MainWindow()
    sys.exit(app.exec_())
