import zmq
import base64
import numpy as np
import cv2
import logging
import sys
import os
import json
from ultralytics import YOLO

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

model_path = "best.pt"
model = YOLO(model_path)
logging.info(f"Model loaded successfully")
logging.info(f"Model device: {model.device}")

address = os.environ.get("ZMQ_ADDRESS", "tcp://localhost:5560")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect(address)
logging.info(f"Server connected to {address}")

while True:
    try:
        msg = socket.recv_string()
        payload = json.loads(msg)

        if "image" not in payload:
            raise ValueError("Missing 'image' field in payload.")

        img_bytes = base64.b64decode(payload["image"])
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        results = model(img)[0] 
        detections = []
        for box in results.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])
            xyxy = box.xyxy[0].tolist()
            detections.append({
                "label": label,
                "confidence": round(conf, 4),
                "box": [round(x, 2) for x in xyxy]
            })

        response = {
            "status": "success",
            "message": "Inference completed",
            "data": detections
        }

    except Exception as e:
        logging.error(f"[Server Error] {e}")
        response = {
            "status": "error",
            "message": str(e),
            "data": None
        }

    socket.send_json(response)
