'''Beginning Program'''

import cv2

CAP = cv2.VideoCapture(0)
FOURCC = cv2.VideoWriter_fourcc(*'XVID')
OUT = cv2.VideoWriter('output.avi', FOURCC, 20.0, (640, 480))



print(CAP.isOpened())
while CAP.isOpened():
    RET, FRAME = CAP.read()
    if RET:
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #cap.get(cv2.CAP_PROP_FRAME_COUNT)
        OUT.write(FRAME)

        GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Show Your Face', GRAY)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

CAP.release()
OUT.release()
cv2.destroyAllWindows()
