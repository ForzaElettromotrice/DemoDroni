from serverSocket.server import ServerSocket
from interface import UI as droneUI
from dronesHandler import TeamDroni


if __name__ == '__main__':
    server = ServerSocket()
    server.start()
    input("Premi qualcosa per chiudere...\n")
    server.stop()
    

