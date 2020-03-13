'''This Program is about an image reading and putting various things on it'''
import cv2

IMG = cv2.imread('./sample/img/face.jpeg', 1)#import the picture

#one can use rgp colour picker to replace the color channel
IMG = cv2.line(IMG, (0, 0), (255, 255), (255, 0, 0), 2)

IMG = cv2.arrowedLine(IMG, (0, 0), (150, 150), (255, 0, 0), 5)#second type of line

IMG = cv2.rectangle(IMG, (0, 0), (200, 200), (255, 0, 0), 5)#draw a rectangle

IMG = cv2.circle(IMG, (100, 100), 50, (255, 0, 0), 6)#draw a circle

FONT = cv2.FONT_HERSHEY_COMPLEX #declaring the font

IMG = cv2.putText(IMG, 'A', (100, 100), FONT, 4, (0, 255, 0), 4, cv2.LINE_AA)#put text on the pic

#showing the picture
cv2.imshow('image', IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()
