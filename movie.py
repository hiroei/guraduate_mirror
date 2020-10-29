#!/usr/bin/env python
"""
動画の特徴点移動を表示するプログラム
"""

import numpy as np
import cv2
import os

def cal_match(im1, im2):
    """
    マッチングの検出
    """
    #特徴抽出機の生成
    detector = cv2.AKAZE_create()#cv2.xfeatures2d.SIFT_create()
    #kpは特徴的な点の位置 destは特徴を現すベクトル
    kp1, des1 = detector.detectAndCompute(im1, None)
    kp2, des2 = detector.detectAndCompute(im2, None)
    matcher = cv2.DescriptorMatcher_create("BruteForce")
    matches = matcher.match(des1,des2)

    return kp1, kp2, matches

def draw_matches(out, kp1, kp2, matches):
 #マッチングに対して繰り返し
    for mat in matches:

        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx
        dis = mat.distance

        (x1, y1) = kp1[img1_idx].pt
        (x2, y2) = kp2[img2_idx].pt

        if cv2.norm((x1, y1), (x2, y2)) < 155 and abs(y2 - y1) < 80 and dis < 300:
            # cv2.circle(out, (int(x1), int(y1)), 4, (255, 0, 255), 2) #画像1のキーポイント ピンク 左目
            # cv2.circle(out, (int(x2), int(y2)), 4, (255, 255, 0), 2) #画像2のキーポイント　水色　右目
            cv2.line(out, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 1)
    
    return out

path = '..'+os.sep+'src'+os.sep+'2-2R0010095_er.MP4'
cap = cv2.VideoCapture(path)
# print(path)

before_frame = []

while(cap.isOpened()):
    ret, frame = cap.read() #フレームを取得
    count = cap.get(cv2.CAP_PROP_POS_FRAMES)
    print(count)

    height, width = frame.shape[:2]
    # size = (int(width/4), int(height/4))
    size = (480, 240)
    # print(size)
    resized_frame = cv2.resize(frame, size)
    if(count==1.0): 
        # before_frame = resized_frame
        before_frame.append(resized_frame)

    #フレームが６を超えたら５つ前と比較する
    # print('特徴点計算')
    kp1, kp2, matches = cal_match(resized_frame, before_frame[int(count)-1])
    # print('表示')
    out = draw_matches(resized_frame, kp1, kp2, matches)
        
    if(count > 6.0):
        # print('特徴点計算')
        kp1, kp2, matches = cal_match(resized_frame, before_frame[int(count)-5])
        # print('表示')
        out = draw_matches(resized_frame, kp1, kp2, matches)

    cv2.imshow('frame', out)

    # before_frame = resized_frame
    before_frame.append(resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

