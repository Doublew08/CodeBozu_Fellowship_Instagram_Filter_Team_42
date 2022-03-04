import cv2
from cv2 import GaussianBlur
from cv2 import BORDER_DEFAULT 
import numpy as np
import matplotlib.pyplot as pil


def main():

    img = cv2.imread("bozu.png", cv2.IMREAD_COLOR)
    img = grayscale(img)

    img = sobelx(img)

    pil.imshow(img , 'gray')

    pil.show()
    cv2.waitKey(0)

def grayscale(img):
    img[:,:,0] = img[:,:,0] * 0.1140 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.2989
    img[:,:,1] = img[:,:,0] * 0.1140 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.2989
    img[:,:,2] = img[:,:,0] * 0.1140 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.2989

    return img 

def sobelx(img):
    img = cv2.GaussianBlur(img, (3,3), 0)
    imgx = cv2.filter2D(img, cv2.CV_64F , np.array([[-1,0,1],[-2,0,2],[-1,0,1]]))
    imgx = np.absolute(imgx)
    imgx = np.uint8(imgx)

    return imgx

def sobely(img):
    img = cv2.GaussianBlur(img, (3,3), 0)
    imgy = cv2.filter2D(img, cv2.CV_64F , np.array([[1,2,1],[0,0,0],[-1,-2,-1]]))
    imgy = np.absolute(imgy)
    imgy = np.uint8(imgy)
    return imgy

def cannyEdge(img): 

    #Five steps 1.Noise Reduction (Gaussian Blur) 2.Gradients calculation 
    # 3.Non-Maximum suppresion (Removing unwanted pixels)  4.Hysteresis Thresholding

    final = cv2.Canny(img, 100,200)

    return final 

main()