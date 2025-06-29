import zmq
import base64
import cv2
import logging
import sys
import os
import json

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

address = os.environ["ZMQ_ADDRESS"]
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(address)

try:
    img = cv2.imread("./test.jpg")
    if img is None:
        raise Exception("Image file not found.")

    _, buffer = cv2.imencode(".jpg", img)
    img_b64 = base64.b64encode(buffer).decode("utf-8")

    payload = {
        "image": img_b64
    }
    socket.send_string(json.dumps(payload))
    logging.info("Image sent to server")

    response = socket.recv_json()
    if response.get("status") == "success":
        logging.info("Detection result: %s", response["data"])
    else:
        logging.error("Server returned error: %s", response["message"])

except Exception as e:
    logging.error(f"Client error: {e}")
