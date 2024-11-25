import asyncio
import threading
from frame_capture import capture_frames
from classification import classify_frames
from video_stream import video_feed

async def main():
    capture_thread = threading.Thread(target=capture_frames)
    classify_thread = threading.Thread(target=classify_frames)
    capture_thread.start()
    classify_thread.start()

    async with websockets.serve(video_feed, "192.168.164.216", 5000):
        await asyncio.Future()  # Run forever

if __name__ == '__main__':
    asyncio.run(main())
