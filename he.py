'''
Author       : WenChan Li
Date         : 2024-10-06 10:11:52
LastEditors  : WenChan Li
LastEditTime : 2024-10-06 10:43:41
Description  : HEistogram Equalization RGB imgage
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-10-06 10:11:52
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取彩色图像
img = cv2.imread("9.bmp")

# 分割通道
b, g, r = cv2.split(img)

# 计算每个通道的直方图
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# 绘制直方图
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist_b, color='b', label='Blue')
plt.plot(hist_g, color='g', label='Green')
plt.plot(hist_r, color='r', label='Red')
plt.xlim([0, 256])
plt.legend()
plt.show()

# 直方图均衡化
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)

# 合并通道
eq_img = cv2.merge([b_eq, g_eq, r_eq])

# 绘制直方图均衡化后的图像和直方图
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Histogram Equalized Image")
plt.imshow(cv2.cvtColor(eq_img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Histogram of Equalized Image")
plt.hist(eq_img.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("Histogram Equalization", eq_img)
cv2.waitKey(0)
