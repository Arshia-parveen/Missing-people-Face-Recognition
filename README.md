# Find Missing Person using Face Recognition

## List of contents
- ### Title of the project
- ### Solution (Project's Implementation)
- ### Steps to  run this application
- ### Future Scope
- ### Use Cases
- ### Dependencies / Show stopper
- ### Mobile Application
- ### Vote of Thanks

### Title of the project
The title of this project is TRACKER.As the name suggests, Tracker is an  application which helps to track the missing people.

### Objective of this Project
The objective of this project is to help Police track down missing people quickly.In our daily lives, usually to track a missing person , investigation is carried out which requires lot of time.This method of tracking people, is not only  time consuming but also  unsuccessful if the missing person has been shifted/moved to different city/country. This web application helps to track down missing people easily and more efficiently.

### Solution (Project's Implementation)
### 1. Registering New Cases
The first step is to register a new case. This GUI application is built using <b>PyQT5</b> that allows you to collect all relevant information. Here complainant need to fill his/her details and also missing person's details.
Complainant details include Complainant's identity, age, phone number and relation with missing person.
Missing person details include Missing person's identity, age, father's name , phone number and house address.

Complainant's Identity include
(a)Complainant's Name
(b)Path of Complainant's image (remove "" and replace \ with \\)(Example if the path is : "C:\Users\Arshia\Desktop\App\images\Elon Musk.jpg" the it should be entered as C:\\Users\\Arshia\\Desktop\\App\\images\\Elon Musk.jpg)

Missing person's Identity include
(a)Missing person's Name
(b)Path of Missing person's image (remove "" and replace \ with \\)(Example if the path is : "C:\Users\Arshia\Desktop\App\images\Elon Musk.jpg" the it should be entered as C:\\Users\\Arshia\\Desktop\\App\\images\\Elon Musk.jpg)

Kindly note: Image should in ".jpg" format.

Once complainant fill all the details  then he/she need to click on "copy" button  once.
Copy button copies all the images from the "Find missing person using face recognition" folder to "images" Folder.
"images" folder consists of all images of missing people.
Finally, click on "Save" button so that all details are saved successfully.

### 2.Unattended Person
So far we have only taked about how we can register new case using this web application. Now, using this appliaction  we can identify unattended person.
Suppose we find/encounter an unattended person, then we can use this application to identify him/her.
First step is to scan his face using web cam, then if the person was registered earlier as missing person then that unattended person's face is recognized by this application and his/her name is displayed. Then one can handover the unattended person to nearby police station. In this way , we can use this web application to identify unattended person.

### Steps to  run this application
### Prerequisites
import sys
import requests
import io
import os
import shutil
import glob
import PIL
import PyQt5
import base64
import json
import cv2
import numpy
import face_recognition

use github link and clone 
$ cd Find missing person using face recognition
$ pip install -r requirements.txt --no-cache-dir
$ python front_end.py

### Future Scope
We can modify this application and add feature which uses live cctv footage and detects the missing people from the faces recognized through cctv.
We can modify this application and add feature such that once if the missing person is detected/found through this app then notification will be automatically sent to nearest police station and also to the person who raised missing complainant.
We can make the missing person's data availabe across all the police stations.
We can also add a fearure such that if anyone finds any unattended person,then he/she can login into the website ,by sharing his/her live location and by entering his/her phone number.Once OTP verification is done, he/she can scan the person's face and upload. If match is found, then notification will be sent to nearest police station and also to the person who raised complaint.
 
### Use Cases
Instead of going to police station and filing a complaint about the  missing child, here we give access to common people to raise a complaint using this app.
The algorithm identifies the face of an individual and compare with the image provided by the person who raised the complaint.

### Dependencies / Show stopper here
Authentication: Any random person cant raise a false missing complaint as his/her face , phone no and other details will be recorded.
Backup and Restore data to/from Cloud or local database
Efficient Mobile application development

>### Mobile Application
An android application  can also be build but since i didnt have much experience in it , i opted for web application.

### Vote of Thanks
-Special thanks to Vikas Kathunia for motivating and guiding me through out.
