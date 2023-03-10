import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

"pip install cvzone"
"pip install mediapipe"

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

folder = "Data/A"  "Here firdt of all try to take the photo and then it willl move in that folder"
counter = 0

while True:
    sucsess, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgWhite = np.ones((imgsize,imgSize,3),np.vint8)*255
        imgCrop = img[y-offset:y+offset, x-offset:x+offset]

        imgCropShape = imgCrop.shape

        imgWhite[0:imgCrop.shape[0],0:imgCropShape[1]] = imgCrop

        aspectRatio=h/w
        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize

        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(imgSize,hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:hCal + hGap, :] = imgResize




        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image" , img)
    key = cv2.waitkey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)
