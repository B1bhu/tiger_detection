# classify.py
import time
import numpy as np
import tflite_runtime.interpreter as tflite
from config import *
from frame_capture import frame
from notifications.notify import send_notifications_with_cooldown
from cloud.cloud_utils import upload_and_notify

def classify_frames():
    global frame
    try:
        model_path = "/path/to/mobilenetssdv2.tflite"
        lblpath = "/path/to/labelmap.txt"
        min_conf_threshold = 0.9
        
        interpreter = tflite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()

        with open(lblpath, "r") as f:
            labels = [line.strip() for line in f.readlines()]

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        height = input_details[0]['shape'][1]
        width = input_details[0]['shape'][2]
        float_input = (input_details[0]['dtype'] == np.float32)
        input_mean = 127.5
        input_std = 127.5

        while True:
            if frame is not None:
                frame_to_process = frame.copy()

                time.sleep(1)

                image_rgb = cv2.cvtColor(frame_to_process, cv2.COLOR_BGR2RGB)
                imH, imW, _ = frame_to_process.shape
                image_resized = cv2.resize(image_rgb, (width, height))
                input_data = np.expand_dims(image_resized, axis=0)

                if float_input:
                    input_data = (np.float32(input_data) - input_mean) / input_std

                interpreter.set_tensor(input_details[0]['index'], input_data)
                interpreter.invoke()

                boxes = interpreter.get_tensor(output_details[1]['index'])[0]
                classes = interpreter.get_tensor(output_details[3]['index'])[0]
                scores = interpreter.get_tensor(output_details[0]['index'])[0]

                tiger_detected = False
                for i in range(len(scores)):
                    if (scores[i] > min_conf_threshold) and (scores[i] <= 1.0):
                        if labels[int(classes[i])] == "Tiger":
                            tiger_detected = True
                            print(f"Tiger detected")

                            send_notifications_with_cooldown()
                            upload_and_notify(frame_to_process)

                            break

                if not tiger_detected:
                    print("No tiger detected in frame")
    except Exception as e:
        print(f"Error during classification: {e}")
