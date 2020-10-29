import numpy as np
import cv2
import os

path = '..'+os.sep+'src'+os.sep+'2-3R0010094_er.MP4'
cap = cv2.VideoCapture(path)
# print(path)

while(cap.isOpened()):
    ret, frame = cap.read()
    size = (960, 480)
    # print(size)
    resized_frame = cv2.resize(frame, size)

    # gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', resized_frame)
    count = cap.get(cv2.CAP_PROP_POS_FRAMES)
    print(count)
    
    #キー入力
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break
    else:
        continue

cap.release()
cv2.destroyAllWindows()

