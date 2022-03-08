import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def redify(img):
    r, g, b = cv.split(img)
    blank = np.zeros(img.shape[:2], dtype='uint8')
    red = cv.merge([r, blank, blank])
    return red


def greenify(img):
    r, g, b = cv.split(img)
    blank = np.zeros(img.shape[:2], dtype='uint8')
    green = cv.merge([blank, g, blank])
    return green


def blueify(img):
    r, g, b = cv.split(img)
    blank = np.zeros(img.shape[:2], dtype='uint8')
    blue = cv.merge([blank, blank, b])
    return blue


def grayscale(img):
    img = img[:, :, 0] * 0.2989 + 0.5870 * img[:, :, 1] + 0.1140 * img[:, :, 2]
    return img


def negative(img):
    print("neg")
    img[:, :, 0] = 255 - img[:, :, 0]
    img[:, :, 1] = 255 - img[:, :, 1]
    img[:, :, 2] = 255 - img[:, :, 2]
    return img

def apply_threshold(img, threshold):
    img[:, :, :][img[:, :, :][img[:,:,:]] >= threshold] = 255
    img[:, :, :][img[:, :, :][img[:,:,:]] < threshold] = 0
    return img


def andromeda(small, big):
    small_length = small.shape[0]
    small_width = small.shape[1]
    big_length = big.shape[0]
    big_width = big.shape[1]
    limit_1 = int(big_width/2 - small_width/2)
    limit_2 = int(big_width/2 + small_width/2)
    limit_3 = int(big_length/2 - small_length/2)
    limit_4 = int(big_length/2 + small_length/2)
    print(limit_2-limit_1)
    big[limit_3:limit_4, limit_1:limit_2] = small
    return big


