from serverSocket.server import ServerSocket
from interface import UI as droneUI
from dronesHandler import TeamDroni


if __name__ == '__main__':
    server = ServerSocket()
    server.start()
    input("Premi qualcosa per chiudere...\n")
    server.stop()
    team_droni = TeamDroni()
    for i in range(7):
        team_droni.update_drone(i, "connesso", (100*i, 100*i), 50, (50*i, 50*i))
    team_droni.ids[3].stato = "sconnesso"
    team_droni.ids[6].stato = "non operativo"
    team_droni.ids[5].stato = "non operativo"

    droneTestUI = droneUI()
    droneTestUI.createInterface(team_droni)
