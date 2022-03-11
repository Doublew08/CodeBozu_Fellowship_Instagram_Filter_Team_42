from re import X
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("real-hippo.jpeg")
x =cv.cvtColor(img, cv.COLOR_RGB2GRAY)
y =cv.medianBlur(x, 3)
z =cv.adaptiveThreshold(y, 255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 9, 2)
plt.imshow(z)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
