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

## ==> GUI FILE
import webbrowser, os, cv2, datetime
from PyQt5.QtGui import QImage, QPixmap
from ui_main import *
from main import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    # OPEN THE LINKS FROM THE "FOLLOW US" PAGE
    def open_link(link):
        webbrowser.open_new_tab(link)

    # OPEN A NEW WINDOW TO SELECT PATH
    def openDirWindow(self):
        self.dir = QFileDialog.getExistingDirectory(None, 'Select project folder:', 'F:\\', QFileDialog.ShowDirsOnly)
        self.ui.lineEditSettings.setText(str(self.dir))

        self.cursor.execute("SELECT * FROM settings_path")
        liste = self.cursor.fetchall()

        for item in liste:
            for i in item:
                old_path=i
        self.cursor.execute("UPDATE settings_path set path=? where path = ?",(self.dir,old_path))
        self.database.commit()

    # VIDEO FUNC
    def shot_video(self):
        today = datetime.datetime.now()
        date_time = today.strftime("%m-%d-%Y, %H.%M.%S")
        self.ui.video_button.setStyleSheet(u"border: 5px solid  rgb(220, 220, 220);\n"
"	background-color: rgb(180, 0, 0);")

        rval, frame = self.ui.page_home.vc.read()
        if self.dir == "":
            UIFunctions.message_box(self, "Please choose a directory to save the video.")
        file_name =(f"tcGridaVid_{date_time}.mp4")
        #TODO: H264 halihazırda bulunan bir kütüphane olmasına rağmen sorun çıkmasının sebebi anlaşılmalı.
        self.out = cv2.VideoWriter(os.path.join(self.dir, file_name), cv2.VideoWriter_fourcc(*'avc1'), 20, (self.ui.page_home.width(),self.ui.page_home.height()))
        self.out.write(frame)

    def stop_video(self):
        if self.out is None:
            pass
        self.ui.video_button.setStyleSheet(u"	border: 5px solid rgb(180, 0, 0);\n"
"	background-color: rgb(58, 8, 8);")
        self.out.release()

    # TAKE SNAPSHOT
    def take_photo(self):
        today = datetime.datetime.now()
        date_time = today.strftime("%m-%d-%Y, %H.%M.%S")
        file_name = (f"tcGrida_{date_time}.jpg")
        # file_name = ("tcGrida_" + dt + str(self.num_photos) + ".jpg")
        print("The photo will be saved as " + file_name)
        rval, frame = self.ui.page_home.vc.read()
        if self.dir == "":
            UIFunctions.message_box(self, "Please choose a directory to save your snapshots.")

        else:
            # TODO: Sanırım app hata vermese bile ve kaydedilecek klasör seçilse de fotoğraflar kaydedilmiyor?? Bunun düzelmesi lazım
            out = cv2.imwrite(os.path.join(self.dir, file_name), frame)
            print("Photo saved to %s"%self.dir)
            print(out)
            # self.num_photos+=1

    def message_box(self, msg):
        message = QMessageBox(self)
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setWindowTitle("Choose a directory")
        message.setText(msg)
        message.setDefaultButton(QMessageBox.Ok)
        message_state = message.exec()
        if(message_state == 1024):
            self.dir = QFileDialog.getExistingDirectory(None, 'Select project folder:', 'F:\\', QFileDialog.ShowDirsOnly)
            self.ui.lineEditSettings.setText(str(self.dir))

            self.cursor.execute("SELECT * FROM settings_path")
            liste = self.cursor.fetchall()

            for item in liste:
                for i in item:
                    old_path=i
            self.cursor.execute("UPDATE settings_path set path=? where path = ?",(self.dir,old_path))
            self.database.commit()

    # CHANGE APPEARANCE
    def change_mode(self):
        self.cursor.execute("SELECT * FROM settings_appearance")
        liste = self.cursor.fetchall()
        for column in liste:
            for item in column:
                old_appearance = item
        if self.ui.toggle.isChecked():
            self.ui.frame.label.setStyleSheet("color: rgb(39, 44, 54)")
            self.ui.frame_2.label.setStyleSheet("color: rgb(39, 44, 54)")
            self.ui.frame_3.label.setStyleSheet("color: rgb(39, 44, 54)")
            self.ui.lineEditSettings.setStyleSheet("background-color: rgb(240, 240, 240); color: rgb(39, 44, 54);")
            self.ui.comboBox.setStyleSheet("background-color: rgb(240, 240, 240); color: rgb(39, 44, 54); selection-background-color: rgb(240, 240, 240);") #rgb(61, 180, 255)
            self.ui.frame.setStyleSheet("background-color : rgb(255, 255, 255);")
            self.ui.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.ui.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.ui.frame_4.setStyleSheet(u"background-color: rgb(240, 240, 240); border-radius: 5px; padding: 10px;")
            self.ui.page_links.label.setStyleSheet("color: rgb(39, 44, 54)")
            self.ui.frame_5.setStyleSheet(u"background-color: rgba(61, 180, 255, 150); border-radius: 5px;")
            #self.ui.frame_grip.setStyleSheet(u"background-color: rgb(173, 130, 0);")
            #self.ui.frame_left_menu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.ui.frame_toggle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.ui.btn_toggle_menu.setStyleSheet(Style.style_btn_toggle.replace("background-color: rgb(27, 29, 35);", "background-color : rgb(61, 180, 255);"))
            self.ui.frame_top_btns.setStyleSheet(u"background-color: rgb(61, 180, 255)") #rgba(0, 73, 174, 200)
            self.ui.frame_top_info.setStyleSheet(u"background-color: rgb(200, 200, 200);")
            self.ui.frame_center.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            #self.ui.frame_left_menu.setStyleSheet(u"background-color: rgb(0, 40, 120);")
            self.ui.frame_content_right.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.ui.label_credits.setStyleSheet(u"color: rgb(40, 40, 40);")
            #self.ui.label_version.setStyleSheet(u"color: rgb(212, 175, 55);")
            self.cursor.execute("UPDATE settings_appearance set appearance=? where appearance = ?",(1,old_appearance))
            self.database.commit()
        else:

            self.ui.frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;\n"
"padding: 10px;"
)
            self.ui.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;\n"
"padding: 10px;"
)
            self.ui.frame_3.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;\n"
"padding: 10px;"
)
            self.ui.frame_4.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
            self.ui.frame_5.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")

            self.ui.page_links.label.setStyleSheet(u"")
            self.ui.frame.label.setStyleSheet(u"")
            self.ui.frame_2.label.setStyleSheet(u"")
            self.ui.frame_3.label.setStyleSheet(u"")
            self.ui.comboBox.setStyleSheet(Style.style_combo)
            self.ui.lineEditSettings.setStyleSheet(Style.style_line)
            self.ui.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")
            #self.ui.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
            self.ui.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
            #self.ui.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
            self.ui.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
            self.ui.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
            #self.ui.btn_toggle_menu.setStyleSheet(Style.style_btn_toggle)
            self.ui.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
            self.ui.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
            #self.ui.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
            self.ui.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
            self.ui.btn_toggle_menu.setStyleSheet(Style.style_btn_toggle)

            self.cursor.execute("UPDATE settings_appearance set appearance=? where appearance = ?",(0,old_appearance))
            self.database.commit()

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus(self):
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setStyleSheet(Style.style_bt_standard.replace("ICON_REPLACE", icon))
        button.setFont(font)
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(61, 180, 255); }") #(44, 49, 60)
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(61, 180, 255); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()


        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())


    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
