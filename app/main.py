import sys
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QSplitter, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFrame
from PyQt5.QtCore import QTimer, Qt
import cv2
import serialVaules

# https://stackoverflow.com/questions/67027784/how-to-open-mainwindow-from-a-splashscreen-without-button-in-pyqt5
# https://learndataanalysis.org/source-code-create-a-modern-style-flash-screen-pyqt5-tutorial/

# Ana pencere
class UI_Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        # Create a timer.
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)

        # Create the main label for camera view.
        self.label = QLabel()
        self.label.setMinimumSize(600, 300)

        # Load USB Camera
        self.openCamUSB()

        # Create buttons
        btnOpen = QPushButton("Bilgisayar kamerasını seç")
        btnOpen.setMinimumSize(25,35)
        btnOpen.setStyleSheet('''
            QPushButton { 
                background-color: #006BFF; 
                color: #93deed; 
                font-size: 15px;
            }
                              
            QPushButton:hover { 
                background-color: #00ABFF; 
                color: #93deed; 
                font-size: 15px;
            }
        ''')

        btnClose = QPushButton("Harici kamerayı seç")
        btnClose.setMinimumSize(25, 35)
        btnClose.setStyleSheet('''
            QPushButton { 
                background-color: #006BFF; 
                color: #93deed; 
                font-size: 15px;
            }

            QPushButton:hover { 
                background-color: #00ABFF; 
                color: #93deed; 
                font-size: 15px;
            }
        ''')

        btnOpen.clicked.connect(self.openCamPC)
        btnClose.clicked.connect(self.openCamUSB)

        # Create a layout.
        layout = QVBoxLayout()
        # Buttons on the top half
        button_layout = QHBoxLayout()
        button_layout.addWidget(btnOpen)

        button_layout.addWidget(btnClose)
        # Bottom half of the screen
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.label)
        # Right half of main_layout
        info_layout = QVBoxLayout()

        '''
        SİLDİĞİM LOADING FONKSIYONU İÇİN OLAN KISIM:
        self.counter = 0
        self.n = 300 # total instances
        self.timerLoad = QTimer()
        self.timerLoad.timeout.connect(self.loading)
        self.timerLoad.start(30)'''

        self.frame = QFrame()

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40)  # x, y
        self.labelTitle.setText('<strong>tcGrida App</strong>')
        self.labelTitle.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(self.labelTitle)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('<strong>Basınç: </strong>' + serialVaules.returnPressure())
        self.labelDescription.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(self.labelDescription)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.labelDescription.y() + 70)
        self.labelLoading.setObjectName('LabelDesc')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('<strong>Nem: </strong>' + serialVaules.returnHumidity())
        info_layout.addWidget(self.labelLoading)

        # Create a logo.
        self.label_logo = QLabel(self.frame)
        self.label_logo.resize(self.width() - 10, 50)  # önceden (self.width() - 10, 50) idi
        self.label_logo.move(0, self.labelLoading.y() + 70)
        self.label_logo.setObjectName('LabelLogo')
        logo_pixmap = QPixmap('logo.png')
        self.label_logo.setPixmap(logo_pixmap)
        self.label_logo.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(self.label_logo)

        # Add them into each other
        layout.addLayout(button_layout)
        layout.addLayout(main_layout)
        main_layout.addLayout(info_layout)

        # Set the layout
        self.setLayout(layout)
        self.setWindowTitle("tcGrida App")
        self.setMinimumSize(700,350)
        self.setWindowIcon(QIcon('logo.png'))

        self.showMaximized()

    def openCamPC(self):
        self.vc = cv2.VideoCapture(0)
        # vc.set(5, 30)  #set FPS
        self.vc.set(3, 800)  # set width
        self.vc.set(4, 650)  # set height
        self.timer.start(round(1000. / 24))

    def openCamUSB(self):
        self.vc = cv2.VideoCapture(1)
        # vc.set(5, 30)  #set FPS
        self.vc.set(3, 800)  # set width
        self.vc.set(4, 650)  # set height
        self.timer.start(round(1000. / 24))

    # https://stackoverflow.com/questions/41103148/capture-webcam-video-using-pyqt
    def nextFrameSlot(self):
        rval, frame = self.vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)


def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(True)

    app.setStyleSheet('''
        #LabelTitle {
            font-size: 60px;
            color: #006BFF;
        }

        #LabelDesc {
            font-size: 30px;
            color: #2F4454;
        }

        QFrame {
            background-color: #c2ced1;
            color: #c2ced1;
        }

    ''')

    ex = UI_Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
