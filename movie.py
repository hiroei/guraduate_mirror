import numpy as np
import cv2
import os

path = '..'+os.sep+'src'+os.sep+'2-2R0010095_er.MP4'
cap = cv2.VideoCapture(path)
# print(path)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    count = cap.get(cv2.CAP_PROP_POS_FRAMES)
    print(count)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

