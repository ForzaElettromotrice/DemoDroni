import socket
import select
import threading
import json


class ServerSocket:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 65000
        self.socket: socket.socket = None

        self.listening = False
        self.l_th: threading.Thread = None
        self.c_ths: list[threading.Thread] = []

    def start(self):
        if not self.socket:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.settimeout(0.5)
        self.listening = True
        self.l_th = threading.Thread(target = self.__listen)
        self.l_th.start()
        print("Started")

    def stop(self):
        self.listening = False

        self.l_th.join()
        for t in self.c_ths:
            t.join()
        self.socket.close()
        print("Stopped")

    def __listen(self):
        self.socket.listen()
        while self.listening:
            try:
                conn, addr = self.socket.accept()
                print(f"Connection with {addr} established!")
                t = threading.Thread(target = self.__receive, args = [conn])
                t.start()
                self.c_ths.append(t)
            except TimeoutError:
                continue

    def __receive(self, conn: socket.socket):
        conn.settimeout(0.5)
        allData = b""
        with conn:
            # Per forzare la chiusura
            while self.listening:
                try:
                    data = conn.recv(4096)
                    allData += data
                    if not data:
                        break
                except TimeoutError:
                    continue
        diz = json.loads(allData.decode("utf-8"))
        _id = diz["id"]
        with open(f"Data{_id}.json", "w") as f:
            json.dump(diz, f, indent = 8)
