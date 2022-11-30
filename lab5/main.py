import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import  sys
from untitled import Window

app = QApplication([])
app.setOrganizationName('Nanjing University')
app.setApplicationName('人工比对工具')
window = Window()
window.ui.show()
app.exec_()