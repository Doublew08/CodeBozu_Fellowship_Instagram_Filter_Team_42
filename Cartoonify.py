from re import X
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("Bozu.png",0)
from rgb import grayscale, apply_threshold
from statistics import mean
def greying(imging):
    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
    imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    return imgGray
x = greying(img)
y =cv.blur(x,(10,10))
z =cv.threshold(img,127,255,cv.THRESH_TOZERO)
#cartoonified = cartoonify(img)
#cv.imwrite("Cartoon",cartoonify(img))
plt.imshow(z)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
