#questo file definisce un drone e un team di droni, main creerà una classe di team di droni, che verrà passato all'interfaccia 
#(oppure direttamente interface durante l'instanza dell'interfaccia ma dovranno essere passati il numero di droni che si vogliono creare)
#poi interface utilizza i valori che la socket riceve
from enum import Enum

class Drone:
    
    def __init__(self, id, stato, pos, batt, obb = None):
        '''Effettua l'inizializazzione degli attributi del drone.
            - id: Identificativo del drone
            - stato: enumerativo
            - batt: percentuale della batteria
            - pos: tupla di coordinate
            - obb: tupla che indica l'obbiettivo'''
        
        self.id = id
        self.stato = stato 
        self.batteria = batt #valore percentuale
        self.posizione = pos  #coordinate posizione

        if obb == None:
            self.obbiettivo = tuple()
        else:
            self.obbiettivo = obb

    #Funzioni di set 
    def set_id(self, ID):
        self.id = ID
    def set_stato(self, stato):
        self.stato = stato
    def set_posizione(self, pos):
        self.posizione = pos
    def set_batteria(self, batt):
        self.batteria = batt
    def set_obbiettivo(self, obb):
        self.obbiettivo = obb

    #Funzioni di get
    def get_id(self):
        return self.id
    def get_stato(self):
        return self.stato
    def get_posizione(self):
        return self.posizione
    def get_batteria(self):
        return self.batteria
    def get_obbiettivo(self):
        return self.obbiettivo
    
class TeamDroni:
    '''Classe che gestice un team di droni.'''
    def __init__(self):
        '''Serve per creare il placeholder per il team di droni.'''
        self.ids = {}
        self.updated = []
    
    def update_drone(self, id, stato = None, pos = None, batt = None, obb = None):
        '''Funzione che aggiorna un drone che ha per id 'id' all'interno del team, e se un valore non viene passato verrà mantenuto il precedente. 
        Nel caso l'id inserito non esista crea un drone che ha come valori quelli passati (se non passati, None)'''
        if id not in self.ids:
            self.ids[id] = Drone(id, stato, pos, batt, obb)
            self.updated.append(id)
            return
        if stato != None:
            self.ids[id].stato = stato
            self.updated.append(id)
        self.ids[id].posizione = (pos if pos != None else self.ids[id].posizione)
        self.ids[id].batteria = (batt if batt != None else self.ids[id].batteria)
        self.ids[id].obbiettivo = (obb if obb != None else self.ids[id].obbiettivo)

class Stato(Enum):
    NOT_OPERATIVE   = "Non operativo"
    NOT_CONNECTED    = "Sconnesso"
    CONNECTED       = "Connesso"
