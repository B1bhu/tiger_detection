# main.py
import threading
import asyncio
from frame_capture.capture import capture_frames
from classification.classify import classify_frames
from websocket.video_stream import start_server

if __name__ == '__main__':
    capture_thread = threading.Thread(target=capture_frames)
    classify_thread = threading.Thread(target=classify_frames)

    capture_thread.start()
    classify_thread.start()

    asyncio.run(start_server())
