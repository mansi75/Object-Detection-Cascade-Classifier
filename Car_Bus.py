import numpy as np
import cv2 as cv

#Load Haar Cascade Classifier
car_cascade = cv.CascadeClassifier("cars.xml")

bus_cascade = cv.CascadeClassifier("bus.xml")

#Load the image
car = cv.imread("car.jpeg")

#Defining object detection function
def object_detection(image, cascadeclassifier, text, color = (255,0,0)):
  
  #Our operation on frame
  gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  
  objects = cv.detectMultiScale(gray, 1.3, 5)
  
  for(x,y, w, h) in objects:
    
    #Draws rectangle around the objects
    
    image = cv.rectangle(image, (x,y), (x+w, y+h), color, 2)
    
    #Display text on the rectangle
    cv.putText(image, text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, 2)
    
    cv.imshow('IMAGE', image)
    
#Car detection

cap = cv.VideoCapture('Cars.mp4')

while(True):
  
  ret, frame = cap.read()
  
  if(type(frame) == type(None)):
    break
    
  object_detection(frame, car_cascade, 'car')
  
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
    
cap.release()

cv.destroyAllWindows()
  
  
  


