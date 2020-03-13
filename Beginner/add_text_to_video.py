'''Basic text addition on video  Program'''
import cv2

CAP = cv2.VideoCapture(0)

print(CAP.get(cv2.CAP_PROP_FRAME_WIDTH))
print(CAP.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(CAP.get(cv2.CAP_PROP_FRAME_COUNT))

CAP.set(3, 1208)
CAP.set(3, 720)

print(CAP.get(3))
print(CAP.get(4))

while CAP.isOpened():
    RET, FRAME = CAP.read()
    if RET:

        GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
        cv2.imshow('YOUR FACE', GRAY)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

CAP.release()
cv2.destroyAllWindows()
