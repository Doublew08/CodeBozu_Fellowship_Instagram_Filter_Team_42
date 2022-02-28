import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.read("real-hippo.jpg", 1)
from rgb import grayscale
def graify(imgto):
 x = grayscale(imgto)
 