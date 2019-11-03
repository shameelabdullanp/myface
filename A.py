import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # wi
cam.set(4, 480) # he

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("\033[1;31;40m	face recognition v1.5(beta) \n\033[1;37;40m") # green
print("\033[5;31;40m	developed by Shameel Abdulla  \033[0;31;40m\n")# blink red
print("\033[1;32;40m	Instructions\n 1- result may change in defferent condition \n") # white
input("	Press Enter to continue...")

#face id set
face_id = input('\n enter user id end press <return> ==>  ')
# define an empty list
places = []
#places.clear()
# open file and read the content in a list
with open('listfile.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        places.append(currentPlace)
newlist=places
name = input("What is your name? ")
newlist.append(name)
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(30) & 0xff #ESC
    if k == 27:
        break
    elif count >= 100: #100 sample
         break

with open('listfile.txt', 'w') as filehandle2:
    for listitem in newlist:
        filehandle2.write('%s\n' % listitem)
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
filehandle2.close()
exec(compile(open('main.py').read(), 'main.py', 'exec'))

