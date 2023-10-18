import cv2

cap = cv2.VideoCapture("C:/Users/Sai Saranya/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/EE26FC66B1369C7625333BEDAFBFCAF6/WhatsApp Video 2023-10-16 at 10.13.26_dc619675.mp4")

if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
