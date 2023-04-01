import cv2

haarcascade_frontalface = cv2.CascadeClassifier('./Faces/haarcascade_frontalface_default.xml')

photo = cv2.imread('./Faces/photo2.jpg', cv2.IMREAD_UNCHANGED)

photoGray = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)

faces = haarcascade_frontalface.detectMultiScale(photoGray,
scaleFactor=1.05,
minNeighbors=5)

for x,y,w,h in faces:
    cv2.rectangle(photo, (x,y), (x+w,y+h), (0,255,0),3)

cv2.imshow('photo', photo)
cv2.waitKey(0)
cv2.destroyAllWindows()