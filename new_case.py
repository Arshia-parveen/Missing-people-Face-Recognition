import sys
import requests
import base64
import json
import cv2
import numpy
import glob
import shutil
import os

from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QImage, QImageReader
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QApplication
from PyQt5.QtWidgets import QInputDialog, QLabel, QLineEdit, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
#python file containing code for "new case registration"
class NewCase(QMainWindow):
    def __init__(self, user: str):
        super().__init__()
        self.title = "NEW CASE REGISTRATION"
        self.name = None
        self.age = None
        self.image=None
        self.phone_number = None
        self.relation=None
        self.image = None
        self.encoded_image = None
        self.key_points = None
        self.user = user
        self.initialize()

    def initialize(self):
        self.setFixedSize(1920,1080)
        self.setWindowTitle(self.title)
        #"Save" button saves all the data
        save_button = QPushButton("SAVE", self)
        save_button.resize(250,45)
        save_button.move(585,675)
        save_button.setFont(QtGui.QFont("Times", 12))
        save_button.clicked.connect(self.save)
        #Copy button copies all the images from the "Find missing person using face recognition" folder to "images" Folder.
        #"images" folder consists of all images of missing people.
        save_button = QPushButton("COPY", self)
        save_button.resize(250,45)
        save_button.move(585,600)
        save_button.setFont(QtGui.QFont("Times", 12))
        save_button.clicked.connect(self.copy)

        self.label_1 = QLabel('Complainant', self)
        self.label_1.move(150,225)
        self.label_1.setStyleSheet(" color:black ;font-size: 11pt")
    
        self.label_2 = QLabel('Missing Person', self)
        self.label_2.move(1050,225)
        self.label_2.setStyleSheet(" color:black ;font-size: 09pt")
        
        #Complainant's Identity include
        #(a)Complainant's Name
        #(b)Path of Complainant's image (remove "" and replace \ with \\)(Example if the path is : "C:\Users\Arshia\Desktop\App\images\Elon Musk.jpg" the it should be entered as C:\\Users\\Arshia\\Desktop\\App\\images\\Elon Musk.jpg)
        identity_1 = QPushButton("Complainant's Identity", self)
        identity_1.setFont(QtGui.QFont("Times", 10))
        identity_1.resize(250,30)
        identity_1.move(150,460)
        identity_1.clicked.connect(self.takename)
        
        #Missing person's Identity include
        #(a)Missing person's Name
        #(b)Path of Missing person's image (remove "" and replace \ with \\)(Example if the path is : "C:\Users\Arshia\Desktop\App\images\Elon Musk.jpg" the it should be entered as C:\\Users\\Arshia\\Desktop\\App\\images\\Elon Musk.jpg)
        identity_2= QPushButton("Missing person's Identity", self)
        identity_2.setFont(QtGui.QFont("Times", 10))
        identity_2.resize(250,30)
        identity_2.move(1050,510)
        identity_2.clicked.connect(self.takename)

        self.get_age()
        self.get_phoneno()
        self.get_relation()
        self.get_ages()
        self.get_father_name()
        self.get_phonenos()
        self.get_address()
        self.show()
    def copy(self):
        src_dir = "C:\\Users\\Arshia\\Desktop\\App"
        dst_dir = "C:\\Users\\Arshia\\Desktop\App\\images"
        for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
            shutil.copy(jpgfile, dst_dir)
  
    def takename(self):
        name1, done1 = QtWidgets.QInputDialog.getText(self, 'Identity', 'Enter name')
        name, done1 = QtWidgets.QInputDialog.getText(self, 'Identity', 'Enter url :')
        img=cv2.imread(name)
        cv2.imshow(name1,img)
        cv2.imwrite(name1+'.jpg',img)

    def get_age(self):
        '''This function takes age as input'''
        self.age = QLabel('Age',self)
        self.age.setStyleSheet(" color:black ; font-size: 11pt")
        self.age.move(150,300)
        self.age_textbox = QLineEdit(self)
        self.age_textbox.resize(200,25)
        self.age_textbox.move(300,305)
        self.age_textbox.setStyleSheet(" color:black ; font-size: 10pt")

    def get_phoneno(self):
        '''This function takes phone number as input'''
        self.phoneno = QLabel('Phone no',self)
        self.phoneno.setStyleSheet(" color:black ; font-size: 11pt")
        self.phoneno.move(150,350)
        self.phoneno_textbox = QLineEdit(self)
        self.phoneno_textbox.resize(200,25)
        self.phoneno_textbox.move(300,355)
        self.phoneno_textbox.setStyleSheet(" color:black ; font-size: 10pt")

    def get_relation(self):
        '''This function takes 'relation with missing people' as input'''
        self.relation = QLabel('Relation',self)
        self.relation.setStyleSheet(" color:black ; font-size: 11pt")
        self.relation.move(150,400)
        self.relation_textbox = QLineEdit(self)
        self.relation_textbox.resize(200,25)
        self.relation_textbox.move(300,405)
        self.relation_textbox.setStyleSheet(" color:black ; font-size: 10pt")

    def get_ages(self):
        '''This function takes age as input'''
        self.ages = QLabel('Age',self)
        self.ages.setStyleSheet(" color:black ; font-size: 11pt")
        self.ages.move(1050,300)
        self.ages_textbox = QLineEdit(self)
        self.ages_textbox.resize(200,25)
        self.ages_textbox.move(1200,305)
        self.ages_textbox.setStyleSheet(" color:black ; font-size: 10pt")
    def get_father_name(self):
        '''This function takes father's name as input'''
        self.father_name = QLabel('Father Name',self)
        self.father_name.setStyleSheet(" color:black ; font-size: 11pt")
        self.father_name.move(1050,350)
        self.father_name_textbox = QLineEdit(self)
        self.father_name_textbox.resize(200,25)
        self.father_name_textbox.move(1200,355)
        self.father_name_textbox.setStyleSheet(" color:black ; font-size: 10pt") 

    def get_phonenos(self):
        '''This function takes phone number as input'''
        self.phonenos = QLabel('Phone no',self)
        self.phonenos.setStyleSheet(" color:black ; font-size: 11pt")
        self.phonenos.move(1050,400)
        self.phonenos_textbox = QLineEdit(self)
        self.phonenos_textbox.resize(200,25)
        self.phonenos_textbox.move(1200,405)
        self.phonenos_textbox.setStyleSheet(" color:black ; font-size: 10pt")

    def get_address(self):
        '''This function takes address as input'''
        self.address = QLabel('Address',self)
        self.address.setStyleSheet(" color:black ; font-size: 11pt")
        self.address.move(1050,450)
        self.address_textbox = QLineEdit(self)
        self.address_textbox.resize(200,25)
        self.address_textbox.move(1200,455)
        self.address_textbox.setStyleSheet(" color:black ; font-size: 10pt")

    def get_entries(self):
        """
        A check to make sure empty fields are not saved.
        A case will be uniquely identified by these fields. 
        """
        entries = {}
        if self.age.text() != "" and self.phoneno.text() != "" and self.name.text() != "" and self.relation.text() != "" and self.names.text() != "" and self.ages.text() != "" and self.father_name.text() != "" and self.phoneno.text() != "" and self.address.text() != "" :
            entries['age'] = self.age.text()
            entries['name'] = self.name.text()
            entries['phoneno'] = self.phoneno.text()
            entries['relation'] = self.relation.text()
            entries['ages'] = self.ages.text()
            entries['names'] = self.names.text()
            entries['father_name'] = self.father_name.text()
            entries['phonenos'] = self.phonenos.text()
            entries['address'] = self.address.text()
            return entries
        else:
            return None
        
    def save(self):
        """
        Save method is triggered with save button on GUI.
       
        All the parameters are passed to a db methods whose task is to save
        them in db.

        If the save operation is successful then you'll get True as output and
        a dialog message will be displayed other False will be returned and
        you'll get appropriate message.

        """
        entries = self.get_entries()
        if entries:
            entries['face_encoding'] = self.key_points
            entries['submitted_by'] = self.user
            entries['case_id'] = generate_uuid()
            self.save_to_db(entries)
        else:
            QMessageBox.about(self, "Error", "Please fill all entries")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = NewCase('Arshia')
    sys.exit(app.exec())
