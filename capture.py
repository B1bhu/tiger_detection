# capture.py
import cv2
import time
from config import *

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

        elapsed_time = time.time() - start_time
        if elapsed_time < interval:
            time.sleep(interval - elapsed_time)
