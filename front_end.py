import sys
import requests
import json
import io

from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListView, QBoxLayout
from PyQt5.QtWidgets import QMessageBox, QListWidget, QLabel, QLineEdit

from new_case import NewCase
from unattended_child import UnattendedChild
#Name of this web application is TRACKER
class AppWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.title = "TRACKER"
        self.width = 1920
        self.height = 1080
        self.user = user
        self.initialize()
    def initialize(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        #Button to register new case
        new_case = QPushButton("NEW CASE", self)
        new_case.move(1200, 200)
        new_case.resize(250, 75)
        new_case.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        new_case.clicked.connect(self.new_case)

        # Button for unattended person's face scan
        unattended_person_case = QPushButton("UNATTENDED PERSON", self)
        unattended_person_case.move(1200, 350)
        unattended_person_case.resize(250, 75)
        unattended_person_case.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        unattended_person_case.clicked.connect(self.unattended_child)
        self.show()
        
    def new_case(self):
        self.new_case = NewCase(self.user)
    def unattended_child(self):
        self.unattended_child=UnattendedChild(self.user)
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow('Arshia')
    sys.exit(app.exec())







    
