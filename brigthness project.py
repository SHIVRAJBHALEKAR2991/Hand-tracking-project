import cv2 as cv
import numpy as np
import handtrackingmodule as htm
import time
import screen_brightness_control as sbc
import math


wcam ,hcam =1920,1080
cap=cv.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
ptime= 0

detector=htm.handDetector(detectioncon=0.7)

while True:
    success,img =cap.read();
    ctime=time.time()
    fps = 1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,f'Fps ={ int (fps)}',(50,50),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
    img =detector.findHands(img,draw=False)
    lmlist = detector.findposition(img, draw=False)



    if len(lmlist)>5:
        print(lmlist[12] , lmlist[9])
        x1,y1 = int(lmlist[12][1]),int(lmlist[12][2])
        x2,y2 =int(lmlist[9][1]), int(lmlist[9][2])

        # cv.circle(img,(int(lmlist[12][1]),int(lmlist[12][2])),5,(0,255,255),cv.FILLED)
        # cv.circle(img, (int(lmlist[9][1]), int(lmlist[9][2])), 5, (0, 255, 255), cv.FILLED)
        # cv.circle(img, ( int((x1+x2)/2) , int((y1+y2)/2)), 5, (0, 255, 255), cv.FILLED)

        # cv.line(img,(x1,y1),(x2,y2),(0, 255, 255),2)
        cv.putText(img, 'Hand Detected', (50,300), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        length = math.hypot(x2 - x1, y2 - y1)
        brightness = sbc.get_brightness()
        cv.putText(img,f'Present:{brightness}',(300,50),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,255),2)

        if length<32:
            # cv.circle(img, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 5, (0, 255, 0), cv.FILLED)
            cv.putText(img,'Min reached',(50,100),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

        if length>100:
            # cv.circle(img, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 5, (0, 255, 0), cv.FILLED)
            cv.putText(img, 'Max reached', (50, 100), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        bright = np.interp(length, [32, 100], [0,100])
        print(bright)
        sbc.set_brightness(bright)





    cv.imshow('image',img)
    cv.waitKey(1)