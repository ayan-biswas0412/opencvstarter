'''Basic fce detector from video Program'''
import cv2

FACE_CASCADE = cv2.CascadeClassifier('./sample/xml/face_detection_basic.xml')
VIDEO_CAPTURE = cv2.VideoCapture(0)


while True:
    _, IMG = VIDEO_CAPTURE.read()
    GRAY_IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
    FACES = FACE_CASCADE.detectMultiScale(GRAY_IMG, scaleFactor=1.05, minNeighbors=4)
    #cv2.imshow('Face detection', GRAY_IMG)
    #cv2.imshow('Face detection', IMG)
    for x, y, w, h in FACES:
        IMG = cv2.rectangle(IMG, (x, y), (x+w, y+h), (0, 255, 0), 4)
        cv2.imshow('Face', IMG)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    



VIDEO_CAPTURE.release()
cv2.destroyAllWindows()





