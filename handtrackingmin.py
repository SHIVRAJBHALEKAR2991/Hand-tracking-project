import cv2 as cv
import  mediapipe as mp
import time

cap=cv.VideoCapture(0)
mpHands=mp.solutions.hands
hands = mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
ptime=0
ctime=0
while  True:
    success,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                print(id ,lm)

                h,w,channels = img.shape
                cx,cy =int(lm.x*w ) ,int(lm.y*h)
                # print( id, cx ,cy)

                if id == 4 or id==8:
                    cv.circle(img,(cx,cy),20,(255,0,255),cv.FILLED)
            mpdraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)


    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime

    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_TRIPLEX,3,(255,0,255),3)


    cv.imshow('image',img)
    cv.waitKey(1)