import cv2

path = "C:/Users/Sai Saranya/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/TempState/697E382CFD25B07A3E62275D3EE132B3/WhatsApp Video 2023-10-16 at 10.23.02_30e492b3.mp4"
cap = cv2.VideoCapture(path)
if not cap.isOpened():
    print("Error opening video file")
else:
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"Height: {height}, Width: {width}, FPS: {fps}")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("frame", frame)
        output.write(frame)
        k = cv2.waitKey(24) & 0xFF
        if k == ord("q"):
            break

    cap.release()
    output.release()
    cv2.destroyAllWindows()
