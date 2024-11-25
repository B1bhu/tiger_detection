# video_stream.py
import cv2
import websockets
import asyncio

async def video_feed(websocket, path):
    global frame
    while True:
        if frame is not None:
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            await websocket.send(frame_bytes)
        await asyncio.sleep(0.1)

async def start_server():
    async with websockets.serve(video_feed, "localhost", 5000):
        await asyncio.Future()  # Keep the server running
