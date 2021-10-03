# -*- coding: utf-8 -*-

import sys

import cv2
from PyQt5.QtWidgets import QApplication,QMainWindow
import Pythonhello

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    myUi = Pythonhello.Ui_MainWindow()
    myUi.setupUi(myMainWindow)

    myMainWindow.show()
    sys.exit(app.exec_())



