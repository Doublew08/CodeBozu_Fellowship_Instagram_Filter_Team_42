import cv2
#import matplotlib.image as mpimg
#import matplotlib.pyplot as plt
import numpy as np
import cv2 
img = cv2.imread('Bozu.png',0)
def flipv(imgg):
    img2= np.zeros([938, 808,], np.uint8)
    for i in range(938):

        img2[i,:]=imgg[938-i-1,:]

    return img2
flipped_v_img=flipv(img)
def fliph(imgg):
    img2 = np.zeros([938,808,], np.uint8)
    for i in range(808):
        img2[:,i]=imgg[:,808-i-1]
    return img2
flipped_h_img = fliph(img)

cv2.imshow('image', flipped_h_img)

cv2.waitKey(0)
cv2.destroyAllWindows()