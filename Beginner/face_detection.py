'''Basic Image analysis Program'''

import cv2

FACE_CASCADE = cv2.CascadeClassifier()
IMG = cv2.imread('./sample/img/face.jpeg', 1)#import the picture
FACES =

cv2.imshow('Face', IMG)





if cv2.waitKey(0) & 0xFF == ord('q'):
    exit() 
#break can only be used to break out of loops so use exit() instead of break

cv2.destroyAllWindows()
