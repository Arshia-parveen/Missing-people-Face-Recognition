import sys
import requests
import base64
import json

from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QImage, QImageReader
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QApplication
from PyQt5.QtWidgets import QInputDialog, QLabel, QLineEdit, QMessageBox

#Python file containing code for unattended child face scan
import cv2
from simple_facerec import SimpleFacerec

class UnattendedChild(QMainWindow):
    def __init__(self, user: str):
        super().__init__()
        self.title = "UNATTENDED CHILD"
        self.user=user
        self.initialize()

    def initialize(self):
        self.setFixedSize(1920,1080)
        self.setWindowTitle(self.title)
        # Record unattended person's face and scan, if matched , name will of unattended child will be displayed
        upload_image = QPushButton("Record Unattended Person's  Image", self)
        upload_image.resize(700,70)
        upload_image.move(600,375)
        upload_image.setFont(QtGui.QFont("Times", 15))
        upload_image.clicked.connect(self.capture)
        self.show()

    def capture(self):
        cap = cv2.VideoCapture(0)
        # Encode faces from a folder
        sfr = SimpleFacerec()
        sfr.load_encoding_images("images/")

       # Load Camera
        while True:
            ret, frame = cap.read()

            # Detect Faces
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

                cv2.imshow("Frame", frame)
 
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UnattendedChild('Arshia')
    sys.exit(app.exec())
