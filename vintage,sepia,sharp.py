import cv2 as cv
import numpy as np
import matplotlib.pyplot as pil

img = cv.imread("Bozu.png", 1)

def vintage(img):
    kx = cv.getGaussianKernel(img.shape[0] , 200)
    ky = cv.getGaussianKernel(img.shape[1] , 200)
    kernel = kx * ky.T
    mask = 255 * kernel / np.linalg.norm(kernel)
    img[:, :, 0] = img[:, :, 0] * mask
    img[:, :, 1] = img[:, :, 1] * mask
    img[:, :, 2] = img[:, :, 2] * mask
    return img

def sepia(img):
    kernel_sepia = np.matrix([[0.272, 0.534, 0.131],
    			    [0.349, 0.686, 0.168],
    			   [0.393, 0.769, 0.189]])
    result = cv.transform(img, kernel_sepia)
    return result

def sharp(img):
    kernel_sharp = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    result = cv.filter2D(img, -1, kernel_sharp)
    return result

result = sharp(sepia(img))

pil.imshow(result)
pil.show()