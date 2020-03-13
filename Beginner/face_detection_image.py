'''Basic Image analysis Program'''

import cv2

FACE_CASCADE = cv2.CascadeClassifier('./sample/xml/face_detection_basic.xml')
IMG = cv2.imread('./sample/img/face.jpeg', 1)#import the picture
GRAY_IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)

FACES = FACE_CASCADE.detectMultiScale(GRAY_IMG, scaleFactor=1.05, minNeighbors=5)

print(type(FACES))
print(FACES)

for x, y, w, h in FACES:
    IMG = cv2.rectangle(IMG, (x, y), (x+w, y+h), (0,0,255), 4)


cv2.imshow('Face', IMG)





if cv2.waitKey(0) & 0xFF == ord('q'):
    exit() 
#break can only be used to break out of loops so use exit() instead of break

cv2.destroyAllWindows()
