import cv2
import time

frame = None

def capture_frames():
    global frame
    cap = cv2.VideoCapture(0)
    fps = 10
    interval = 1.0 / fps

    while True:
        start_time = time.time()
        ret, output = cap.read()
        if ret:
            frame = output.copy()
        time.sleep(max(0, interval - (time.time() - start_time)))
