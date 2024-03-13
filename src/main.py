from serverSocket.server import ServerSocket

if __name__ == '__main__':
    server = ServerSocket()
    server.start()
    input("Premi qualcosa per chiudere...\n")
    server.stop()
