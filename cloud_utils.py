# cloud_utils.py
import time
import cv2
import cloudinary.uploader
from config import *

def upload_and_notify(frame):
    try:
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        response = cloudinary.uploader.upload(frame_bytes, folder="detected_tiger_photos/")
        image_url = response['url']
        print(f"Uploaded image: {image_url}")

        send_api_request_with_cooldown(image_url)
    except Exception as e:
        print(f"Error uploading frame: {e}")

def send_api_request_with_cooldown(image_url):
    try:
        api_url = "http://example.com/api"
        data = {"image_url": image_url}
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            print("API request successful.")
        else:
            print(f"API request failed: {response.status_code}")
    except Exception as e:
        print(f"Error sending API request: {e}")
