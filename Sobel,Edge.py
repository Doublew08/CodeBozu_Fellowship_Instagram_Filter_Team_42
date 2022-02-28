import cv2
from cv2 import GaussianBlur
from cv2 import BORDER_DEFAULT 
import numpy as np
import matplotlib.pyplot as pil


def main():

    img = cv2.imread("bozu.png", cv2.IMREAD_COLOR)

    img = cannyEdge(img)

    pil.imshow(img , 'gray')

    pil.show()
    cv2.waitKey(0)

def sobelx(img):
    img = cv2.GaussianBlur(img, (3,3), 0)
    imgx = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta = 0, borderType=cv2.BORDER_DEFAULT)
    imgx = cv2.convertScaleAbs(imgx)

    return imgx

def sobely(img):
    img = cv2.GaussianBlur(img, (3,3), 0)
    imgy = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta = 0, borderType=cv2.BORDER_DEFAULT)
    imgy = cv2.convertScaleAbs(imgy)

    return imgy

def cannyEdge(img): 

    #Five steps 1.Noise Reduction (Gaussian Blur) 2.Gradients calculation 
    # 3.Non-Maximum suppresion (Removing unwanted pixels)  4.Double threshold
    # 5. Edge tracking 

    img = cv2.Canny(img, 100, 200)

    return img

main()