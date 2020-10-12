import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     #loading the the face detecting file
img = cv2.imread('test.png')                                                    # reading the image
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                    # converting the image to grey scale
faces = face_cascade.detectMultiScale(grey, 1.2, 2)                             # detecting faces, return the coordinates of faces in a form of rectungular coordinates

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)                                                          # displaying image
cv2.waitKey()                                                                   # closing image on a press of a key
