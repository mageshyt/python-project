from cv2 import *
from random import randrange
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#importing the image
# img=cv2.imread('./img/Csk.jpg')
img=cv2.imread('./img/Csk.jpg')
#img=cv2.imread('./img/Csk.jpeg')

#video
cap= cv2.VideoCapture(0)
#Must convert image to greay
grayScalled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect Face
face_coording=trained_face_data.detectMultiScale(grayScalled_img)

# Color Choice
color=[]
# Darw face rectangle
# [[ 983  258  949  949]]
#    x    y    w     h
for x,y,width,height in face_coording:
    cv2.rectangle(img,(x, y),(x+width,y+height),(randrange(128,256),randrange(256),randrange(256)),5)

#image Show
cv2.imshow('Face detctor',img)
cv2.waitKey()
#print("code Completed",face_coording)


