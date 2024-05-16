import cv2 as cv
import  mediapipe as mp
import time

class handDetector():
    def __init__(self,mode =False ,maxhands=2,detectioncon=0.5,trackcon=0.5):
        self.mode=mode
        self.maxhands=maxhands
        self.detectioncon= int(detectioncon)
        self.trackcon= int(trackcon)

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxhands,self.detectioncon,self.trackcon)
        self.mpdraw = mp.solutions.drawing_utils

    def findHands(self,img,draw =True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if (draw):

                    self.mpdraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)

        return  img

    def findposition(self,img,handno=0,draw=True):
        lmList=[]

        if self.results.multi_hand_landmarks:
            myhand =self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):
                # print(id ,lm)

                h, w, channels = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id,cx,cy))


                if draw:
                    cv.circle(img, (cx, cy), 10, (255, 0, 255), cv.FILLED)




        return lmList



def main():
    ptime = 0
    ctime = 0
    cap = cv.VideoCapture(0)
    detector=handDetector()
    while True:
        success, img = cap.read()

        img = detector.findHands(img)
        lmlist =detector.findposition(img)
        if len(lmlist)!=0:

            print(lmlist[4])


        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_TRIPLEX, 3, (255, 0, 255), 3)

        cv.imshow('image', img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()