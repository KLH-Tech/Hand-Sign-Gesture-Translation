import os
from os import listdir
from os.path import isfile, join
from this import d
import numpy
import cv2

d=0

mypath="D:\WorkSpace\....." # Enter your dataset images path here 

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)

# To take image from file 
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) ) 

for i in images:
  scale_percent = 500 # percent of original size
  width = int(i.shape[1] * scale_percent / 100)
  height = int(i.shape[0] * scale_percent / 100)
  dim = (width, height)
  resiz=cv2.resize(i, dim , interpolation=cv2.INTER_AREA) # resize images 
  gray = cv2.cvtColor(resiz,cv2.COLOR_BGR2GRAY) # converting to gray scale 
  blur = cv2.GaussianBlur(gray,(9,9),sigmaX=8,sigmaY=8)
  thresh = cv2.adaptiveThreshold(blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  cv2.THRESH_BINARY_INV, 21, 4)
  ret,res = cv2.threshold(thresh, 10, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

  # Enter the path to store the converted images
  path = 'data\....' 
  
  cv2.imwrite(os.path.join(path , '%d.jpg'%d),res)
  d+=1  # names the stored images with 0,1,2,3......
  cv2.waitKey(0)
