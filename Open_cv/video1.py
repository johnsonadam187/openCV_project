import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import cv2


cap = cv2.VideoCapture(r"C:\Users\johns\Videos\Captures\Drop shift left hook.mp4", cv2.IMREAD_GRAYSCALE)


while True:
  ret, frame = cap.read()
  cv2.imshow("frame", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()