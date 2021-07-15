# -*- coding: utf-8 -*-
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

import cv2
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QImage, QImageReader, QImageWriter, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QCursor)
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from qtwidgets import AnimatedToggle
from ui_styles import Style
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        # Aşırı alakasız toggle kodu. 
        self.toggle = AnimatedToggle(
                checked_color="#007fff",
               
        )
        

        self.toggle.setObjectName(u"toggle")

        # Toggle bitiyor, mainwindow buradan devam ediyor.
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(Style.style_frame_main)
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle_menu.setStyleSheet(Style.style_btn_toggle)

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-drop.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")

        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        ## PHOTO BUTTON
        self.photo_button = QPushButton(self.frame_extra_menus)
        self.photo_button.setObjectName(u"PHOTO")
        self.photo_button.setToolTip("Take a snapshot!")
        self.photo_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.photo_button.setIcon(icon3) #border: 5px solid rgb(15, 16, 20)
        self.photo_button.setStyleSheet(Style.style_circ_btn)

        self.layout_menu_bottom.addWidget(self.photo_button, 0, Qt.AlignHCenter)

        # VIDEO BUTTON

        self.video_button = QPushButton(self.frame_extra_menus)
        self.video_button.setObjectName(u"VIDEO")
        self.video_button.setToolTip("Record a video!")
        self.video_button.setCursor(QCursor(Qt.PointingHandCursor))
        #icon3 = QIcon()
        #icon3.addFile(u":/16x16/icons/16x16/cil-camera.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.video_button.setIcon(icon3) #border: 5px solid rgb(15, 16, 20)
        self.video_button.setText("REC")
        self.video_button.setStyleSheet(Style.style_circ_btn2)

        self.layout_menu_bottom.addWidget(self.video_button, 0, Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        ###################################################
        ## HOME PAGE
        ###################################################

        ## NOT: Arduino ile kablosuz bağlantı kurarsak basınç vs. değerleri sayısal olarak home'daki görüntünün üstünde
        ## göstermek için cv2.putText(frame, dt,
        ##                    (10, 100),
        ##                    font, 1,
        ##                    (210, 155, 155), 
        ##                    4, cv2.LINE_8) şeklinde yazabiliriz. dt = datetime

        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.page_home.label = QLabel()
        self.page_home.label.setObjectName(u"label")
        #self. = QFont()
        #self..setFamily(u"Segoe UI")
        #self..setPointSize(14)
        #self.label.setFont(self.)
        self.page_home.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.page_home.label)

        self.stackedWidget.addWidget(self.page_home)

        ###################################################
        ## INFO PAGE
        ###################################################

        #TODO: Add info page.
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayoutInfo =QVBoxLayout(self.page_info)
        self.verticalLayoutInfo.setObjectName(u"verticalLayoutInfo")
        
        self.label = QLabel()
        self.label.setObjectName(u"frame_label")

        self.font6 = QFont()
        self.font6.setFamily(u"Segoe UI")
        self.font6.setPointSize(14)
        self.label.setFont(self.font6)

        self.label.setText("Coming Soon!")

        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayoutInfo.addWidget(self.label)
        

        self.stackedWidget.addWidget(self.page_info)

        ###################################################
        ## SETTINGS PAGE
        ###################################################

        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayoutSettings = QVBoxLayout(self.page_settings)
        self.verticalLayoutSettings.setObjectName(u"verticalLayoutSettings")

        self.frame = QFrame(self.page_settings)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;\n"
"padding: 10px;"
)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        # TITLE

        self.frame.label = QLabel()
        self.frame.label.setObjectName(u"frame_label")
        self.frame.label.setFont(self.font6)

        self.frame.label.setText("Choose which directory your snapshots will be saved to:")
        self.frame.label.setOpenExternalLinks(True)
        self.frame.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.frame.label)

        self.lineEditSettings = QLineEdit(self.frame)
        self.lineEditSettings.setObjectName(u"lineEditSettings")
        self.lineEditSettings.setMinimumSize(QSize(0, 30))
        self.lineEditSettings.setStyleSheet(Style.style_line)

        self.horizontalLayout_11.addWidget(self.lineEditSettings)

        self.pushButtonSettings = QPushButton(self.frame)
        self.pushButtonSettings.setObjectName(u"pushButtonSettings")
        self.pushButtonSettings.setMinimumSize(QSize(150, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.pushButtonSettings.setFont(font8)
        self.pushButtonSettings.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"       margin-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSettings.setIcon(icon3)

        self.horizontalLayout_11.addWidget(self.pushButtonSettings)
        self.verticalLayout_15.addLayout(self.horizontalLayout_11)
        self.verticalLayoutSettings.addWidget(self.frame)

        ## CHOOSE CAM
        self.frame_2 = QFrame(self.page_settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;\n"
"padding: 10px;"
)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        # TITLE

        self.frame_2.label = QLabel()
        self.frame_2.label.setObjectName(u"frame2_label")

        self.frame_2.label.setFont(self.font6)

        self.frame_2.label.setText("Choose which camera will be captured:")
        self.frame_2.label.setOpenExternalLinks(True)
        self.frame_2.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.frame_2.label)

        # ...

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font8)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(Style.style_combo)
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)
        self.verticalLayout_11.addWidget(self.comboBox)
        self.verticalLayoutSettings.addWidget(self.frame_2)

        ## DETERMINE LIGHT OR DARK MODE
        self.frame_3 = QFrame(self.page_settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;\n"
"padding: 10px;"
)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)

        # TITLE

        self.frame_3.label = QLabel()
        self.frame_3.label.setObjectName(u"frame3_label")

        self.frame_3.label.setFont(self.font6)

        self.frame_3.label.setText("Appearance:")
        self.frame_3.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.frame_3.label)

        self.frame_3.space = QLabel()
        self.frame_3.space.setStyleSheet(u"	border-radius: 10px;	\n"
"	background-color: rgb(39, 44, 54);")
        #self.frame_3.space.setText("D̲A̲R̲K̲ ̲M̲O̲D̲E̲")
        self.frame_3.space.setAlignment(Qt.AlignRight)
        self.frame_3.space2 = QLabel()
        self.frame_3.space2.setStyleSheet(u"	border-radius: 10px;	\n"
"	background-color: rgb(39, 44, 54);")
        #self.frame_3.space2.setText("L̲I̲G̲H̲T̲ ̲M̲O̲D̲E̲")
        self.frame_3.space2.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_12.addWidget(self.frame_3.space)
        self.horizontalLayout_12.addWidget(self.toggle)
        self.horizontalLayout_12.addWidget(self.frame_3.space2)

        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")


        self.verticalLayoutSettings.addWidget(self.frame_3)

        ###################################################
        ## "FOLLOW US" PAGE
        ###################################################

        self.page_links = QWidget()
        self.page_links.setObjectName(u"page_links")
        
        self.frame_4 = QFrame(self.page_links)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.frame_5 = QFrame(self.page_links)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_links = QHBoxLayout(self.page_links)
        self.horizontalLayout_links.setObjectName(u"horizontalLayout_links")
        self.horizontalLayout_links.addWidget(self.frame_4)
        self.horizontalLayout_links.addWidget(self.frame_5)

        self.verticalLayout_links = QVBoxLayout(self.frame_4)
        self.verticalLayout_links.setObjectName(u"verticalLayout_links")
        self.verticalLayout_links.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setAlignment(Qt.AlignCenter)

        ## TODO: Bu logo neden görünmüyor?
        self.page_links.logo = QLabel(self.frame_4)
        self.page_links.logo.setObjectName(u"label_logo")
        self.page_links.logo.setAlignment(Qt.AlignCenter)
        logo_image = QImage("url(:/16x16/icons/cil-logo.png)")
        logo_pixmap = QPixmap.fromImage(logo_image)
        self.page_links.logo.setPixmap(logo_pixmap)
        self.page_links.logo.resize(logo_pixmap.width(), logo_pixmap.height())

        self.verticalLayout_links.addWidget(self.page_links.logo)

        # TITLE

        self.page_links.label = QLabel(self.frame_4)
        self.page_links.label.setObjectName(u"label")

        self.page_links.label.setFont(self.font6)
        self.page_links.label.setText("KEEP UP WITH OUR LATEST UPDATES! ")
        self.page_links.label.setOpenExternalLinks(True)
        self.page_links.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_links.addWidget(self.page_links.label)

        self.stackedWidget.addWidget(self.page_links)

        # LINK BUTTONS - INSTAGRAM

        self.instaLinkButton = QCommandLinkButton(self.frame_4)
        self.instaLinkButton.setText("Our Instagram Page!")
        self.instaLinkButton.setObjectName(u"instaLinkButton")
        self.instaLinkButton.setStyleSheet(u"QCommandLinkButton:hover {\n"
"	background-color: rgb(30,35,40);	\n"
"}")
        self.instaLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instaLinkButton.setIcon(icon4)

        self.instaLinkButton.setDescription("Instagram")

        self.verticalLayout_links.addWidget(self.instaLinkButton, alignment = Qt.AlignCenter)

        # LINK BUTTONS - GITHUB

        self.gitLinkButton = QCommandLinkButton(self.frame_4)
        self.gitLinkButton.setText("Our Github Page!")
        self.gitLinkButton.setObjectName(u"gitLinkButton")
        self.gitLinkButton.setStyleSheet(u"QCommandLinkButton:hover {\n"
"	background-color: rgb(30,35,40);	\n"
"}")
        self.gitLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gitLinkButton.setIcon(icon4)

        self.gitLinkButton.setDescription("Github")

        self.verticalLayout_links.addWidget(self.gitLinkButton, alignment = Qt.AlignCenter)

        # LINK BUTTONS - WEBSITE
        
        self.webLinkButton=QCommandLinkButton(self.frame_4)
        self.webLinkButton.setText("Our Website!")
        self.webLinkButton.setObjectName(u"webLinkButton")
        self.webLinkButton.setStyleSheet(u"QCommandLinkButton:hover {\n"
"	background-color: rgb(30,35,40);	\n"
"}")
        self.webLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.webLinkButton.setIcon(icon4)

        self.webLinkButton.setDescription("Website")
        
        self.verticalLayout_links.addWidget(self.webLinkButton, alignment = Qt.AlignCenter)

        # LINK BUTTONS - YOUTUBE
        self.youtubeLinkButton=QCommandLinkButton(self.frame_4)
        self.youtubeLinkButton.setText("Our Youtube Channel!")
        self.youtubeLinkButton.setObjectName(u"youtubeLinkButton")
        self.youtubeLinkButton.setStyleSheet(u"QCommandLinkButton:hover {\n"
"	background-color: rgb(30,35,40);	\n"
"}")
        self.youtubeLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.youtubeLinkButton.setIcon(icon4)

        self.youtubeLinkButton.setDescription("Youtube")

        self.verticalLayout_links.addWidget(self.youtubeLinkButton, alignment=Qt.AlignCenter)

        # LINK BUTTONS - FORM

        self.formLinkButton = QCommandLinkButton(self.frame_4)
        self.formLinkButton.setText("Feedback Form!")
        self.formLinkButton.setObjectName(u"formLinkButton")
        self.formLinkButton.setStyleSheet(u"QCommandLinkButton:hover {\n"
"	background-color: rgb(30,35,40);	\n"
"}")
        self.formLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.formLinkButton.setIcon(icon4)

        self.formLinkButton.setDescription("Any Comments?")

        self.verticalLayout_links.addWidget(self.formLinkButton, alignment = Qt.AlignCenter)

        # TODO: Bu yol ile embed oluyor ama app üzerinde kötü gözüküyor.
        self.webview=QWebEngineView()
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.webview.page().fullScreenRequested.connect(lambda request: request.accept())
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/01ofdSy_Puo"))
        self.verticalLayout_13.addWidget(self.webview)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.toggle)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"tcGrida App", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"PC Camera 0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"USB Camera 1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"USB Camera 2", None))

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Antalya ISAS", None))
    # retranslateUi
