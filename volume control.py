import cv2 as cv
import time
import numpy as np
import handtrackingmodule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wcam ,hcam =640,480
cap=cv.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
ptime= 0

detector=htm.handDetector(detectioncon=0.7)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volrange=volume.GetVolumeRange()
minvol=volrange[0]
maxvol = volrange[1]



while True:
    success,img=cap.read()
    ctime=time.time()
    fps = 1/(ctime-ptime)
    ptime=ctime

    img =detector.findHands(img)

    lmlist =detector.findposition(img,draw=False)
    # print(lmlist)
    if (len(lmlist)>20):
        # print(lmlist[4] , lmlist[8])
        x1 ,y1 =lmlist[4][1],lmlist[4][2]
        x2,y2 =lmlist[8][1], lmlist[8][2]
        cx ,cy =int((x1+x2)/2) , int((y1+y2)/2)
        cv.circle(img,(lmlist[4][1],lmlist[4][2]),10,(255,0,0),cv.FILLED)
        cv.circle(img, (lmlist[8][1], lmlist[8][2]), 10, (255, 0, 0), cv.FILLED)
        cv.circle(img,( int((x1+x2)/2) , int((y1+y2)/2)),10,(255,0,0),cv.FILLED)
        cv.line(img,(lmlist[4][1],lmlist[4][2]),(lmlist[8][1],lmlist[8][2]),(255,0,0),2)

        length = math.hypot(x2-x1 ,y2-y1)
        print(int(length))
        if length <30:
            cv.circle(img, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 10, (0, 255, 0), cv.FILLED)

        if length>200:
            cv.circle(img, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 10, (0, 255, 0), cv.FILLED)

        vol=np.interp(length,[30,200],[minvol,maxvol])
        print(vol)

        volume.SetMasterVolumeLevel(vol, None)

    cv.putText(img,f'FPS {int(fps)}',(50,50),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),thickness=2)



    cv.imshow("image",img)
    cv.waitKey(1)