import numpy as np
import cv2 as cv

#Load all Haar Cascade Classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

fullbody_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')

#Loads all the required images
img = cv.imread("face.jpeg")

body = cv.imread("body.jpeg")

#Defining Object Detection Function
def object_detection(image, cascade, text, color = (255,0,0)):
 
  #Our operation on frame
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
  objects = cascade.detectMultiScale(gray, 1.3, 5)
  
  for(x, y, w, h) in objects:
    
    #Draw rectangle around the boxes
    img = cv.rectangle(img, (x,y), (x+w, y+h), color, 2)
    
    #Display text on top of the rectangle
    cv.putText(img, text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    #Display the resulting image
    cv.imshow('IMAGE', img)
    
#Face detection
object_detection(img, face_cascade, 'face')

cv.waitKey(0)

#Eye detection
object_detection(img, eye_cascade, 'eye')

cv.waitKey(0)

cv.destroyAllWindows()
                     
