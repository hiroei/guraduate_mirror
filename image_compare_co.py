#!/usr/bin/env python
"""
動画
"""

import numpy as np
import cv2
import os

path = '..'+os.sep+'src'+os.sep+'frame1.png'
path2 = '..'+os.sep+'src'+os.sep+'frame2.png'

im1 = cv2.imread(path)
im2 = cv2.imread(path2)
height, width = im1.shape[:2]

gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
ori_im1 = gray1

# dstimg = cv2.addWeighted(src1=gray1, alpha=0.5, src2=gray2, beta=0.5, gamma=0)
# cv2.imshow('dst', dstimg)

angle = 0 #回転角
while(True):
    #画像の回転処理
    # if(angle!=0):
    height, width = gray1.shape[:2]
    cut_place = (width/4) * angle
    print(cut_place)
    right_cut = (int(cut_place), int(width))
    left_cut = (0, int(cut_place))
    img1 = gray1[0:480, 2:960] #右
    img2 = gray1[0:480, 0:2]   #左
    
    gray1 = cv2.hconcat([img1, img2])

    dstimg = cv2.addWeighted(src1=gray1, alpha=0.5, src2=gray2, beta=0.5, gamma=0)
    cv2.imshow('frame', dstimg)
    print(angle)
    # print(count)
    #キー入力
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        angle += 1
        if angle > 3:
            angle = 0
            # gray1 = ori_im1
        continue
    else:
        continue

# cv2.waitKey(0)

cv2.destroyAllWindows()