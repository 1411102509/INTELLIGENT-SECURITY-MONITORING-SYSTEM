from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initTimer()

    def initTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_pic)

    def show_pic(self):
        ret, img = self.vc.read()
        if not ret:
            print('文件读取错误!\n')
            return
        cv2.flip(img, 1, img)
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.lbl.setPixmap(pixmap)

    def openCamera(self):
        self.lbl.setEnabled(True)
        self.vc = cv2.VideoCapture(0)
        self.openCameraBtn.setEnabled(False)
        self.closeCameraBtn.setEnabled(True)
        self.timer.start(100)

    def closeCamera(self):
        self.vc.release()
        self.openCameraBtn.setEnabled(True)
        self.closeCameraBtn.setEnabled(False)
        self.QLable_close()
        self.timer.stop()

    def initUI(self):
        self.openCameraBtn = QPushButton('打开摄像头')
        self.openCameraBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.openCameraBtn.clicked.connect(self.openCamera)
        self.closeCameraBtn = QPushButton('关闭摄像头')
        self.closeCameraBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.closeCameraBtn.clicked.connect(self.closeCamera)
        self.openCameraBtn.setEnabled(True)
        self.closeCameraBtn.setEnabled(False)
        self.lbl = QLabel(self)
        self.lbl.resize(200, 100)
        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.lbl)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.openCameraBtn)
        self.vbox.addWidget(self.closeCameraBtn)
        self.hbox.addLayout(self.vbox)

        self.setLayout(self.hbox)
        self.QLable_close()
        self.move(300, 300)
        self.setWindowTitle('OPENCV')
        self.setGeometry(300, 300, 500, 250)
        self.show()

    def QLable_close(self):
        self.lbl.setStyleSheet("background:black;")
        self.lbl.setPixmap(QPixmap())

    def start(self):
        self.timer.start(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())