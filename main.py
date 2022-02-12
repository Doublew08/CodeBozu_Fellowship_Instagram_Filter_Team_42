import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from rgb import redify, greenify, blueify, grayscale, negative

bad = False

img = mpimg.imread("Bakery.jpg")
result = img

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
        result = grayscale(img)
        plt.imshow(result, cmap="gray")
    elif op == "5":
        result = negative(img)
        plt.imshow(result)
    else:
        bad = False

plt.show()
