import cv2
import face_recogntion
import pickle
from datetime import datetime

#Create an instance of the VideoCapture class
cap = cv2.VideoCapture(0)

#Set the image width and heigth
width, height = 320, 240

#Set the format of the captured image
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#Create a face detector using the HAAR cascade classifier
face_cascade = cv2.CascadeClassifier(
	"haar_cascade_files/haarcascade_frontalface_default.xml")

#Prompt the user to enter the name for the registered face
name = input("Enter your name: ")

#Prompt the user to enter the room access (comma-seperated)
access_input = input("Enter room access (comma-seperated): ")
access_list = access_input.split(',')

#Initialize an empty list to store the face data
face_data = []

#Counter for the number of face captures
captures_count = 0

while True:
  #Capture frame-by-frame
  ret, frame = cap.read()
  
  #Convert the frame to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  #Detect faces in the frame
  faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5, minSize = (30, 30))
  
  #Draw rectangles around the detected faces
  for(x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
  
  #Encode the face region of internet (ROI) using face
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  face_encodings = face_recognition.face_encodings(rgb_frame,[(y, x+w, y+h, x)])
  
  #Store the face region of interest
  for face_encoding in face_encodings:
     face_data.append({"name": name, "face": frame[y:y+h, x:x+w], "face_encoding": face_encoding, "access": access_list})
