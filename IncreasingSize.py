import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('Rtest50x50.png', 1)        
w, h = img.shape[:2]
xNew = int(w * 2)
yNew = int(h * 2)
xScale = xNew/(w-1)
yScale = yNew/(h-1)
newImage = np.zeros([xNew, yNew,3])
 
for i in range(xNew-1):
   for j in range(yNew-1):
       newImage[i + 1, j + 1]= img[1 + int(i / xScale),
                                 1 + int(j / yScale)]
cv.imwrite('scaled.png', newImage)

plt.imshow(newImage)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
