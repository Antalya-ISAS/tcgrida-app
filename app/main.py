import sys
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QSplitter, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFrame
from PyQt5.QtCore import QTimer, Qt
import cv2

# https://stackoverflow.com/questions/67027784/how-to-open-mainwindow-from-a-splashscreen-without-button-in-pyqt5
# https://learndataanalysis.org/source-code-create-a-modern-style-flash-screen-pyqt5-tutorial/

# Ana pencere
class UI_Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
 
        self.setStyleSheet("background-color: black;")
        
        # Create a timer.
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)

        # Create the main label for camera view.
        self.label = QLabel()
        self.label.resize(self.width() - 35, 150)
        self.label.move(0, self.height() - 100)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.showMaximized()

        # Load USB Camera
        self.openCamUSB()

        # Create buttons
        btnOpen = QPushButton("Bilgisayar kamerasını seç")
        btnOpen.setMinimumSize(25, 35)
        btnOpen.setStyleSheet('''
            QPushButton { 
                background-color: #006BFF; 
                color: #93deed; 
                font-size: 15px;
                border-style:none;
                border:1px solid #3f3f3f; 
                padding:5px;
                min-height:20px;
                border-radius:15px;

            }
            QPushButton:hover { 
                background-color: #00ABFF; 
                color: #93deed; 
                font-size: 15px;
                border-style:none;
                border:1px solid #3f3f3f; 
                padding:5px;
                min-height:20px;
                border-radius:15px;
            }
        ''')

        btnClose = QPushButton("Harici kamerayı seç")
        btnClose.setMinimumSize(25, 35)
        btnClose.setStyleSheet('''
            QPushButton { 
                background-color: #006BFF; 
                color: #93deed; 
                font-size: 15px;
                border-style:none;
                border:1px solid #3f3f3f; 
                padding:5px;
                min-height:20px;
                border-radius:15px;

            }
            QPushButton:hover { 
                background-color: #00ABFF; 
                color: #93deed; 
                font-size: 15px;
                border-style:none;
                border:1px solid #3f3f3f; 
                padding:5px;
                min-height:20px;
                border-radius:15px;
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

        self.frame = QFrame()

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40)  # x, y
        self.labelTitle.setText('<strong>tcGrida App</strong>')
        self.labelTitle.setAlignment(Qt.AlignCenter)

        # Bottom half of the screen
        layout.addWidget(self.labelTitle)
        layout.addLayout(button_layout)
        layout.addWidget(self.label)

        # Set the layout
        self.setLayout(layout)
        self.setWindowTitle("tcGrida App")
        self.setMinimumSize(700, 350)
        self.setWindowIcon(QIcon('logo.png'))

        self.showMaximized()

    def openCamPC(self):
        self.vc = cv2.VideoCapture(0)
        # vc.set(5, 30)  #set FPS
        self.vc.set(3, 4000)  # set width
        self.vc.set(4, 1500)  # set height
        self.timer.start(round(1000. / 24))

    def openCamUSB(self):
        self.vc = cv2.VideoCapture(1)
        # vc.set(5, 30)  #set FPS
        self.vc.set(3, 4000)  # set width
        self.vc.set(4, 1500)  # set height
        self.timer.start(round(1000. / 24))

    # https://stackoverflow.com/questions/41103148/capture-webcam-video-using-pyqt
    def nextFrameSlot(self):
        rval, frame = self.vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resize = cv2.cv2.resize(frame, (1300, 1000))
        image = QImage(resize, resize.shape[1], resize.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
       # logo_pixmap = cv2.cv2.imread('logo.png')
       # dst = cv2.addWeighted(frame,1.0,logo_pixmap,0.7,0) #bu satır düzeltilecek

        self.label.setPixmap(pixmap)


def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(True)

    app.setStyleSheet('''
        #LabelTitle {
            font-size: 45px;
            color: #006BFF;
        }
        #LabelDesc {
            font-size: 30px;
            color: #c2ced1;
        }
        QFrame {
            background-color: #2F4454;
            color: #2F4454;
        }
    ''')

    ex = UI_Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
