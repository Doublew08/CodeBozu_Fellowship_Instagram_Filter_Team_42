import numpy as np
import cv2 as cv


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
    r, g, b = cv.split(img)
    result = r * 0.2989 + 0.5870 * g + 0.1140 * b
    return result


def negative(img):
    r, g, b = cv.split(img)
    r = 255 - r
    g = 255 - g
    b = 255 - b
    result = cv.merge([r, g, b])
    return result
