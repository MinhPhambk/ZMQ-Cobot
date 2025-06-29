import zmq
import os
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

client_address = os.environ["ZMQ_CLIENT_ADDRESS"]
server_address = os.environ["ZMQ_SERVER_ADDRESS"]

def main():
    context = zmq.Context(1)
    frontend = context.socket(zmq.ROUTER)
    frontend.bind(client_address)
    backend = context.socket(zmq.DEALER)
    backend.bind(server_address)

    logging.info(f"Device started: {client_address} ⇄ {server_address}")
    zmq.proxy(frontend, backend)

if __name__ == "__main__":
    main()
