import json
import random
import socket

if __name__ == '__main__':
    HOST = "127.0.0.1"
    PORT = 65000

    diz = { "id": random.randint(0, 10), "name": "Matteo", "age": 21, "sex": "gay" }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(bytes(json.dumps(diz), "utf-8"))

    print("Closed")
