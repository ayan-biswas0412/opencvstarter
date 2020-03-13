'''This Program is about an video and various processes on it'''

import cv2
import time

VIDEO = cv2.VideoCapture(0)

a=1
while True:
    a=a+1
    CHECK, FRAME = VIDEO.read()

    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_RGB2GRAY)
    #print(CHECK)
    #print(FRAME)
    cv2.imshow('Capturing', FRAME)
    KEY = cv2.waitKey(1)
    if KEY == ord('q'):
        break


time.sleep(1)


print(a)
VIDEO.release()
cv2.destroyAllWindows()
