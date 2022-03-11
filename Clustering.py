from re import X
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("real-hippo.jpeg")
def clusterimage(image,k):
    i = np.float32(image).reshape(-1,3)
    condition = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,20,1.0)
    ret,label,center = cv.kmeans(i, k , None, condition,10,cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    final_img = center[label.flatten()]
    final_img = final_img.reshape(image.shape)
    return final_img
plt.imshow(clusterimage(img,6))
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()