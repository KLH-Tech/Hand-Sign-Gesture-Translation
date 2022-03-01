import numpy as np
import cv2

vid = cv2.VideoCapture(0)
while True:
  sucess, img = vid.read()
  #use if want in GRAY scale 
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #For Canny edge detection
  #edges = cv2.Canny(gray,100,200)
  thresh = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4) #converts the Grey image to thresholding
  ret,res = cv2.threshold(thresh, 10, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) # converts the Grey image to Adaptive thresholding
  cv2.imshow("Video",res) 
  if cv2.waitKey(1) & 0xFF == ord('q') :
    break