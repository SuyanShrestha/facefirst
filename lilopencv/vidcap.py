import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
#0 le chahi webcam through capture garxa, existing vid file ko name rakhdina ni paiyo

while True:
    flg, img = cap.read() 
    #first var gives flag that fram read correctly or nah, and second var gives frame itself

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #grayscale img matra detect garni vara convert normal to grayscale

    thops = face_cascade.detectMultiScale(gray, 1.5, 4)
    #this func takes 3 arguments, first is grayscale image, ani scale factor, ani minimum neighbours

    for(x, y, w, h) in thops:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,215,0), 2)
        #4 arguments, img, min coordinates, max coordinates, color and thickness of rectangle

    cv2.imshow('img', img)          #display image

    k = cv2.waitKey(30) & 0xff      #0xff le chahi leaves only last 8 bits of original
    if k==27:
        break  #press Esc to break, due to waitKey

cap.release()

