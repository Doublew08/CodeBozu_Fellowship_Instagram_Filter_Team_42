import numpy as np
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("Bozu.png", 1)
print(src)
print(src.shape)

blue = src[:, :, 0]
green = src[:, :, 1]
red = src[:, :, 2]

blue_img = np.zeros(src.shape)
# print(src[:, :, 3].shape)
blue_img[:, :, 0] = blue
# blue_img[:, :, 3] = np.zeros(src[:, :, 3].shape)
print(blue_img)
cv2.imwrite("blue.png", blue_img)
