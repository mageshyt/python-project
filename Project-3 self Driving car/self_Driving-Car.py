import cv2

#Video
video=cv2.VideoCapture('./Video/Tesla_Autopilot_Dashcam_Compilation_2018_Version_online_video_cutter.mp4')

# Our image
img_file = './img/car-4.jpeg'

# Our pre trained cart calssfier
car_classifier_file = './car_detctor.xml'
human_classifier_file='./haarcascade_fullbody.xml'
# Create open cv img
img = cv2.imread(img_file)

#create car classifier
car_tracker=cv2.CascadeClassifier(car_classifier_file)
human_tracker=cv2.CascadeClassifier(human_classifier_file)
#Must convert image to greay
black_n_white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#car detctor
#car=car_tracker.detectMultiScale(black_n_white)
 
#iterating each and every frame
while True:
    #read the current frame
    (read_succesful,frame)=video.read()
    #Safe coding.
    if read_succesful:
        grayed_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else :
        break
    #detect car and human
    cars=car_tracker.detectMultiScale(frame)
    humans=human_tracker.detectMultiScale(frame)
    #print(cars)

#For cars
    for (x,y,width,height) in cars:
        cv2.rectangle(frame,(x,y),(x+width,y+height),(0,0,255),3)
#for human
    for (x,y,width,height) in humans:
        cv2.rectangle(frame,(x,y),(x+width,y+height),(0,255,255),3)
    #Disply the image with the faces spotted
    cv2.imshow('Self Driving car',frame)
    # #dont autoClose =>wait till press any key and then close
    key= cv2.waitKey(1)
    if key==81 or key==113: #Press Q to exit
        break
video.release()
# # Draw rectangle

# for (x,y,width,height) in car:
#     cv2.rectangle(img,(x,y),(x+width,y+height),(0,0,225),5)
# print(car)
# #To Shoe image
# cv2.imshow('car Detctor' , video)

# # #dont autoClose =>wait till press any key and then close
# cv2.waitKey(1)

# print("Code Completed")
