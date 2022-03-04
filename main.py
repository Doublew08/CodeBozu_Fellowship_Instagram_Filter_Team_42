import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2 as cv
from rgb import redify, greenify, blueify, grayscale, negative, apply_threshold, andromeda

bad = False

img = cv.imread("Bozu.png", 1)
plt.imshow(img)
plt.show()

while bad is False:
    bad = True
    op = input("What do you want to do (choose the number from the list)? Options are\n1: Red-only photo\n" +
           "2: Green-only photo\n" + "3: Blue-only photo\n" + "4: Grayscale photo\n" + "5: Negative photo\n")
    if op == "1":
        x = redify(img)
        plt.imshow(x)
    elif op == "2":
        result = greenify(img)
        plt.imshow(result)
    elif op == "3":
        result = blueify(img)
        plt.imshow(result)
    elif op == "4":
        x = grayscale(img)
        plt.imshow(x)
    elif op == "5":
        result = negative(img)
        plt.imshow(result)
    elif op == "6":
        threshold = input("Enter the threshold: \n")
        result = apply_threshold(img, int(threshold))
        plt.imshow(result)
    elif op == "7":
        big = cv.imread("Bakery.jpg")
        small = cv.imread("Bozu.png")
        result = andromeda(small, big)
        plt.imshow(result)
    else:
        bad = False


plt.show()
