import cv2
import cv2
import numpy as np
import argparse
import imutils



#ap=argparse.ArgumentParser()
#ap.add_argument("-i", "--video", required=True, help="path to the input image")
#args= vars(ap.parse_args())
video = cv2.videoCapture(0)
objekti_leidmine= cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=100)
while True:
    net, frame=video.read()
    mask= objekti_leidmine.apply(frame)
    _,mask = cv2.threshold(mask, 245,255,cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask,cv2.RETR_THREE, cv2.CHAIN)
    detect=[];
    for cnt in contours:
        pnd=cv2.contourArea(cnt)
        x,y,w,h=cv2.boundingReact(cnt)
        keskel =cv2.center(cnt)






        cv2.imshow("video",frame)