# api_utils.py
import requests
from config import *

def send_api_request(image_url):
    try:
        api_url = "http://example.com/api"
        data = {
            "image_url": image_url,
            "latitude": latitude,
            "longitude": longitude
        }
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            print("API request successful")
        else:
            print(f"API request failed: {response.status_code}")
    except Exception as e:
        print(f"API request failed: {e}")
