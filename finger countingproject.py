import cv2 as cv
import time
import handtrackingmodule as htm
import os

wcam,hcam=640,480
cap=cv.VideoCapture(0)
cap.set(3,wcam)
cap.set(4 ,hcam)
ptime=0

detector=htm.handDetector()

while True:
    success,img =cap.read()
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(img,f'fps {int (fps)}',(400,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),2)

    img=detector.findHands(img,draw=False)
    lmlist=detector.findposition(img,draw=False)
    if (len(lmlist)>=20):
        if ((lmlist[4][2] < lmlist[2][2]) and (lmlist[8][2] > lmlist[6][2]) and (lmlist[12][2] > lmlist[10][2]) and (
                lmlist[16][2] > lmlist[14][2] and (lmlist[20][2] > lmlist[18][2]))):
            print(0)
            cv.putText(img, "0", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0), 3)

        if((lmlist[4][2]<lmlist[2][2]) and(lmlist[8][2]<lmlist[6][2]) and(lmlist[12][2]>lmlist[10][2])and(lmlist[16][2]>lmlist[14][2] and(lmlist[20][2]>lmlist[18][2]))):
            print(1)
            cv.putText(img,"1",(50,50),cv.FONT_HERSHEY_TRIPLEX,2,(0,255,0),3)

        if ((lmlist[4][2] < lmlist[2][2]) and (lmlist[8][2] < lmlist[6][2]) and (lmlist[12][2] < lmlist[10][2]) and (lmlist[16][2] > lmlist[14][2] and (lmlist[20][2] > lmlist[18][2]))):
            print(2)
            cv.putText(img, "2", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0), 3)

        if ((lmlist[4][2] < lmlist[2][2]) and (lmlist[8][2] < lmlist[6][2]) and (lmlist[12][2] < lmlist[10][2]) and (
                lmlist[16][2] < lmlist[14][2] and (lmlist[20][2] > lmlist[18][2]))):
            print(3)
            cv.putText(img, "3", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0), 3)

        if ((lmlist[4][2] > lmlist[5][2]) and (lmlist[4][2] < lmlist[2][2]) and (lmlist[8][2] < lmlist[6][2]) and (lmlist[12][2] < lmlist[10][2]) and (
                lmlist[16][2] < lmlist[14][2] and (lmlist[20][2] < lmlist[18][2]))):
            print(4)
            cv.putText(img, "4", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0), 3)

        if ((lmlist[4][2] < lmlist[5][2])and(lmlist[4][2] < lmlist[2][2]) and (lmlist[8][2] < lmlist[6][2]) and (lmlist[12][2] < lmlist[10][2]) and (
                lmlist[16][2] < lmlist[14][2] and (lmlist[20][2] < lmlist[18][2]))):
            print(5)
            cv.putText(img, "5", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0), 3)





        # if ((lmlist[4][1] < lmlist[3][1]) and (lmlist[8][2] < lmlist[6][2]) and (lmlist[12][2] < lmlist[10][2]) and (
        #         lmlist[16][2] > lmlist[14][2] and (lmlist[20][2] > lmlist[18][2]))):
        #     print(5)
        #     cv.putText(img, "5", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 0), 3)









    cv.imshow("image",img)
    cv.waitKey(1)