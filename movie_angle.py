#!/usr/bin/env python
"""
動画の角度を回転させるプログラム
"""

import numpy as np
import cv2
import os

path = '..'+os.sep+'src'+os.sep+'2-2R0010095_er.MP4'
cap = cv2.VideoCapture(path)
# print(path)

angle = 0 #回転角
size = (960, 480)

while(cap.isOpened()):
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, size)

    #画像の回転処理
    if(angle!=0):
        height, width = resized_frame.shape[:2]
        cut_place = (width/4) * angle
        print(cut_place)
        right_cut = (int(cut_place), int(width))
        left_cut = (0, int(cut_place))
        img1 = resized_frame[0:480, right_cut[0]:right_cut[1]] #右
        img2 = resized_frame[0:480, left_cut[0]:left_cut[1]]   #左
    
        resized_frame = cv2.hconcat([img1, img2])


    cv2.imshow('frame', resized_frame)
    count = cap.get(cv2.CAP_PROP_POS_FRAMES)
    # print(count)
    #キー入力
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        angle += 1
        if angle > 3:
            angle = 0
        continue
    else:
        continue

cap.release()
cv2.destroyAllWindows()

