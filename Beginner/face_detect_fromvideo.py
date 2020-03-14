'''Basic fce detector from video Program'''
import cv2

FACE_CASCADE = cv2.CascadeClassifier('./sample/xml/face_detection_basic.xml')
VIDEO_CAPTURE = cv2.VideoCapture(0)


while True:
    _, IMG = VIDEO_CAPTURE.read()
    FACES = FACE_CASCADE.detectMultiScale(IMG, scaleFactor=1.05, minNeighbors=4)
    for x, y, w, h in FACES:
        IMG = cv2.rectangle(IMG, (x, y), (x+w, y+h), (0, 255, 0), 4)
        FLIP_IMAGE = cv2.flip(IMG, 1)
        cv2.imshow('Face', FLIP_IMAGE)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
VIDEO_CAPTURE.release()
cv2.destroyAllWindows()





