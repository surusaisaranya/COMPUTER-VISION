import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/Sai Saranya/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/FFEDF5BE3A86E2EE281D54CDC97BC1CF/WhatsApp Video 2023-10-17 at 08.59.54_ebc0fcd8.mp4")
while True:
 ret, frame = cap.read()
 pts1 = np.float32([[200,300], [5, 2],[0, 4], [6, 0]])
 pts2 = np.float32([[0, 0], [4, 0],[0, 1], [4, 6]])
 matrix = cv2.getPerspectiveTransform(pts1, pts2)
 result = cv2.warpPerspective(frame, matrix, (5,5))
 cv2.imshow('frcame', frame) # Initial Capture
 cv2.imshow('frame1', result) # Transformed Capture
 if cv2.waitKey(24) == 27:
   break
 cap.release()
 cv2.destroyAllWindows()
