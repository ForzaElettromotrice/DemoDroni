#questo file definisce un drone e un team di droni, main creerà una classe di team di droni, che verrà passato all'interfaccia 
#(oppure direttamente interface durante l'instanza dell'interfaccia ma dovranno essere passati il numero di droni che si vogliono creare)
#poi interface utilizza i valori che la socket riceve
from enum import Enum


class Stato(Enum):
    """Classe enumeratore che specifica gli stati che può assumere un drone.

    Si utilizza importando Stato e semplicemente richiamando gli elementi
    dell'enumeratore tramite Stato."attribute".
        
=========
ATTRIBUTI
=========

    :attr NOT_OPERATIVE: Per quando lo stato del drone è non operativo
    :attr NOT_CONNECTED: Per quando lo stato del drone è sconnesso
    :attr CONNECTED: Per quando lo stato del drone è connesso 
    """
    NOT_OPERATIVE = "Non operativo"
    NOT_CONNECTED = "Sconnesso"
    CONNECTED = "Connesso"

class Drone:
    """Classe che modella un drone e mantiene le sue informazioni principali.

    I droni vengono creati e gestiti dalla classe TeamDroni.

=========
ATTRIBUTI
=========

    :attr id: Parametro che prende un int che indica l'id del drone.
    :type id: int
    :attr stato: Parametro che prende un elemento dell'enumerativo Stato.
    :type stato: Stato 
    :attr batt: Parametro che prende un int che indica la batteria del drone.
    :type batt: int
    :attr pos: tupla di coordinate.
    :type pos: (int, int)
    :attr obb: tupla che indica l'obbiettivo.
    :type obb: (int, int) 
    """
    
    def __init__(self, id: int, stato: Stato, pos: tuple, batt: int, 
                 obb: tuple = None) -> None:
        """Costruttore che effettua l'inizializazzione degli 
        attributi del drone.

=========
PARAMETRI
=========
        
        :param id: Parametro che prende un int che indica l'id del drone.
        :type id: int
        :param stato: Parametro che prende uno elemento.
        dell'enumerativo Stato.
        :type stato: Stato 
        :param batt: Parametro che prende un int che indica la 
        batteria del drone.
        :type batt: int
        :param pos: tupla di coordinate.
        :type pos: (int, int)
        :param obb: tupla che indica l'obbiettivo.
        :type obb: (int, int)
        """
        
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
    """Classe che gestice un team di droni.
    
    TeamDroni serve per inizializzare un team di droni che poi andranno a
    compiere le loro missioni di perlustrazione. Gestisce l'input dei valori
    degli attributi della classe drone.

=========
ATTRIBUTI
=========

    :attr ids: Contiene le coppie (id, drone)
    :type ids: Dizionario
    :attr updated: Droni nuovi al team o che hanno recentemente cambio stato. 
    Serve per poter aggiornare le icone presenti nella GUI.
    :type updated: Lista
    """

    def __init__(self):
        """Serve per creare il placeholder per il team di droni.
        """
        self.ids = {}
        self.updated = []
    
    def update_drone(self, id: int, stato: Stato = None, pos: tuple = None, batt: int = None, 
                     obb: tuple = None) -> None:
        """Funzione che aggiorna un drone.
         
        Deve essere passato un id 'id', e se un drone all'interno del team 
        ha id 'id', quel drone verrà aggiornato con i restanti valor passati
        nei parametri, e se un valore non viene passato verrà mantenuto il 
        precedente. Nel caso l'id inserito non esista crea un drone che ha 
        come valori quelli passati, e se non passati, None.

=========
PARAMETRI
=========

        :param id: ID di un drone, che sia da aggiungere o aggiornare.
        :type id: int, required.
        :param stato: Uno stato che verrà assegnato al drone con id ID.
        :type stato: Un elemento dell'enumeratore Stato.
        :param pos: Una tupla che indica la posizione attuale del drone.
        :type pos: Tupla di coordinate.
        :param batt: La batteria del drone.
        :type batt: int.
        :param obb: Locazione in cui si sta spostando il drone.
        :type obb: Tupla di coordinate. 
        """
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
