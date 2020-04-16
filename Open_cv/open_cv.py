import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import cv2

img = cv2.imread(r"C:\Users\johns\Pictures\Saved Pictures\evanholy.jpg", cv2.IMREAD_COLOR)
cv2.rectangle(img, (10,10), (150, 150), (255, 0, 0), 5)
cv2.circle(img, (75, 75), 75, (0, 255, 0), 5)
cv2.imshow("Holyfield vs Tyson", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

