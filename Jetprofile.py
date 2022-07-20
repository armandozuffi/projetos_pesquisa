import cv2
import numpy as np

img = cv2.imread('phase.bmp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)