'''
Author       : WenChan Li
Date         : 2024-10-06 11:04:58
LastEditors  : WenChan Li
LastEditTime : 2024-10-06 20:03:59
Description  : 
Copyright 2024 OBKoro1, All Rights Reserved. 
2024-10-06 11:04:58
'''
import numpy as np
import cv2


def replaceZeroes(data):
    #np.nonzero(a)返回目标数组a中非零元素的索引
    min_nonzero = min(data[np.nonzero(data)])
    data[data == 0] = min_nonzero  ##如果像素值为0，就用最小的像素值代替
    return data


def SSR(src_img, sigmaX):
    #获得与原图大小相同的 高斯模糊 后的图片，用以近似illumination L(x,y)
    L = cv2.GaussianBlur(src_img, (0, 0), sigmaX)
    #参数size是指卷积核的大小，这里设置为0，表示模型从后面的参数sigmax自动计算。
    #同理也可以写成L = cv2.GaussianBlur(src_img, (size,size), 0)由size计算sigama

    #用最小值代替数组中的0
    img = replaceZeroes(src_img)
    L = replaceZeroes(L)

    #获得log_R =log_I - log_L
    log_img = cv2.log(img / 1.0)  #转成浮点数才能进行log操作
    log_L = cv2.log(L / 1.0)
    log_R = cv2.subtract(log_img, log_L)

    #指定将图片的值放缩到 0-255 之间
    dst_R = cv2.normalize(log_R, None, 0, 255, cv2.NORM_MINMAX)
    '''
    #上面一行代码的平替
    min_v,max_v,min_i,max_i = cv2.minMaxLoc(log_R)#返回矩阵的最小值，最大值，并得到最大值，最小值的索引

    h,w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            log_R[i,j] = (log_R[i,j] - min_v)*255.0/ (max_v - min_v)
    '''

    #缩放，获取绝对值，转换为无符号的8位类型
    log_uint8 = cv2.convertScaleAbs(dst_R)

    return log_uint8


if __name__ == '__main__':
    img_path = './3.bmp'
    sigma = 65
    src_img = cv2.imread(img_path)

    b_gray, g_gray, r_gray = cv2.split(src_img)
    b_gray = SSR(b_gray, sigma)
    g_gray = SSR(g_gray, sigma)
    r_gray = SSR(r_gray, sigma)
    result = cv2.merge([b_gray, g_gray, r_gray])

    # cv2.namedWindow("img", cv2.WINDOW_NORMAL)  #调整窗口大小
    # cv2.resizeWindow("img", 800, 600)
    # cv2.imshow('img', src_img)

    # cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("result", 800, 600)
    # cv2.imshow('result', result)

    # print("over")
    # cv2.waitKey(0)
    cv2.imwrite('result3.jpg', result)
