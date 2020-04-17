import cv2
import numpy as np


img = cv2.imread(r"C:\Users\johns\Pictures\Saved Pictures\Holyfield.jpg", cv2.IMREAD_GRAYSCALE)
retval, threshold = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY_INV)

#gaussian adaptive threshold
gaus = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('gaussian', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()