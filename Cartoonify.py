import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("real-hippo.png")
from rgb import grayscale, apply_threshold

def cartoonify(imgto):
 x = grayscale(imgto)
 y =cv2.blur(x,(10,10))
 z =apply_threshold(y,50)
 return x
cartoonified = grayscale(img)

plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
