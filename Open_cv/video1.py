import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import cv2


cap = cv2.VideoCapture(r"C:\Users\johns\Videos\Captures\Drop shift left hook.mp4")


while True:
  ret, frame = cap.read()
  grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow("frame", grayframe)

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()