# -*- coding: utf-8 -*-
"""Image_Capture_&_Labelled_faces_in_the_wild.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1318N23P-XR3UBzMykL0vS24FferK8Yfr

**Importing necessary librarires**
"""

import cv2
import os
import random
import numpy as np
import matplotlib.pyplot as plt

"""**Setting path of anchor positive and negative folder**"""

pos_path = os.path.join('data', 'positive')
neg_path = os.path.join('data', 'negative')
anc_path = os.path.join('data', 'anchor')

"""**Prepare directories to save images**"""

os.makedirs(pos_path)
os.makedirs(neg_path)
os.makedirs(anc_path)

"""**Downloading labelled face in wild lfw dataset**"""

# !wget http://vis-www.cs.umass.edu/lfw/lfw.tgz

"""**Unzipping the folder**"""

!tar -xf lfw.tgz

# #Move lfw images to the negative folder
for dir in os.listdir(r'C:\Users\artem\Downloads\archive.zip\lfw-deepfunneled\lfw-deepfunneled'):
    for file in os.listdir(os.path.join(r'C:\Users\artem\Downloads\archive.zip\lfw-deepfunneled\lfw-deepfunneled', dir)):
        ex_path = os.path.join(r'C:\Users\artem\Downloads\archive.zip\lfw-deepfunneled\lfw-deepfunneled', dir, file)
        new_path = os.path.join(neg_path, file)
        os.replace(ex_path, new_path)

# If above doesn't work then download directly from web and do following
import shutil

source = r'D:\python\face recognition\New folder'; destination = neg_path

for dirs in os.listdir(source):
    for file in os.listdir(os.path.join(source, dirs)):
        shutil.copy(os.path.join(source, dirs, file), destination)


# import shutil
# src_files = os.listdir('/content/sample_data')
# for file_name in src_files:
#     full_file_name = os.path.join('/content/sample_data', file_name)
#     if os.path.isfile(full_file_name):
#         shutil.copy(full_file_name, '/content/drive/MyDrive/new/data/negative')

"""Import uuid lib to uniquely name the images that is captured from webcam"""

#Import uuid library to generate unique image names
import uuid #universally unique identifier

#Establish a connection to webcam
cap = cv2.VideoCapture(0) #0 means the webcam of laptop
while cap.isOpened():
    ret, frame = cap.read()

    #cut down frames to 250x250 px
    frame = frame[50:300,250:500,:] #taing a frame of 250,250,3(rgb) frame to capture image

    #Collect Anchors
    if cv2.waitKey(1) & 0XFF == ord('a'):
        img_name = os.path.join(anc_path, f'{uuid.uuid1()}.jpg' )
        cv2.imwrite(img_name, frame)

    #Collect positives
    if cv2.waitKey(1) & 0XFF == ord('p'):
        img_name = os.path.join(pos_path, f'{uuid.uuid1()}.jpg' )
        cv2.imwrite(img_name, frame)

    #Show img to screen
    cv2.imshow('Image Collection', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

plt.imshow(frame)
