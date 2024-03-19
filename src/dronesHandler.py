#questo file definisce un drone e un team di droni, main creerà una classe di team di droni, che verrà passato all'interfaccia 
#(oppure direttamente interface durante l'instanza dell'interfaccia ma dovranno essere passati il numero di droni che si vogliono creare)
#poi interface utilizza i valori che la socket riceve

class drone:
    
    def __init__(self, id, stato, pos, batt):
        '''Effettua l'inizializazzione degli attributi del drone.
            - id: Identificativo del drone
            - stato: enumerativo
            - pos: tupla di coordinate
            - batt: percentuale della batteria'''
        self.id = id
        self.stato = stato #0: non attivo    1: non connesso, attivo     2: connesso, attivo
        self.posizione = pos  #coordinate posizione
        self.batteria = batt #valore percentuale
