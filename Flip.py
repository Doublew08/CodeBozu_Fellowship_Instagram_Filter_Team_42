import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Bozu.png', 1)


def flip_vertical(imgg):
    shaper = imgg.shape
    img2 = np.zeros([shaper[0], shaper[1], 3], np.uint8)
    for i in range(shaper[0]):
        img2[i, :, :] = imgg[shaper[0]-i-1, :, :]
    return img2


flipped_v_img = flip_vertical(img)


def flip_horizontal(imgg):
    shaper = imgg.shape
    img2 = np.zeros([shaper[0], shaper[1], 3], np.uint8)
    for i in range(shaper[1]):
        img2[:, i, :] = imgg[:, shaper[1]-i-1, :]
    return img2


def headshot(img):
    shaper = img.shape
    img2 = np.zeros([int(shaper[0] / 2), shaper[1], 3], np.uint8)
    for i in range(int(shaper[0] / 2)):
        img2[i, :, :] = img[i, :, :]
    return img2


head_bozu = headshot(img)
flipped_h_img = flip_horizontal(img)

plt.imshow(flipped_h_img)
plt.show()
plt.imshow(flipped_v_img)
plt.show()
plt.imshow(head_bozu)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()