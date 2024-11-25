import time
import numpy as np
import tflite_runtime.interpreter as tflite
from notifications import send_sms, send_email
from frame_capture import frame

def classify_frames():
    model_path = "../data/mobilenetssdv2.tflite"
    lbl_path = "../data/labelmap.txt"
    min_conf_threshold = 0.9

    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    with open(lbl_path, "r") as f:
        labels = [line.strip() for line in f.readlines()]

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    width, height = input_details[0]['shape'][2], input_details[0]['shape'][1]
    float_input = (input_details[0]['dtype'] == np.float32)
    
    while True:
        if frame is not None:
            process_frame(interpreter, labels, float_input, height, width)

def process_frame(interpreter, labels, float_input, height, width):
    # Frame processing logic here
    pass
