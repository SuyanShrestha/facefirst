import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img= cv2.imread('dummyimg5.webp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#grayscale img matra detect garni vara convert normal to grayscale

thops = face_cascade.detectMultiScale(gray, 1.5, 4)
#this func takes 3 arguments, first is grayscale image, ani scale factor, ani minimum neighbours

for(x, y, w, h) in thops:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,215,0), 2)
    #4 arguments, img, min coordinates, max coordinates, color and thickness of rectangle

cv2.imshow('img', img)          #display image

cv2.waitKey()