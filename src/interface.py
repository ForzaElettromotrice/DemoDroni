import dearpygui.dearpygui as dpg
import dearpygui_map as map #libreria estensione di dpg per la mappa per MATTEO, fa cagare 
from screeninfo import get_monitors
from dronesHandler import TeamDroni, Stato


class UI:
    '''Classe che gestisce l'interfaccia utente, mappa compresa.
    
    Deve essere seguito il costruttore, poi interface() e infine setup() a cui va passato l'oggetto team_droni.'''
    #tags contiene i tag non gestiti da dpg, cioè solo quello della mappa, che tanto MATTEO deve cambiare
    #tags = {}

    #variabili di classe per dearpygui
    screenSize = (get_monitors()[0].width, get_monitors()[0].height)
    connected = dpg.load_image("src/dronesImg/droneConnected.png")
    not_connected = dpg.load_image("src/dronesImg/droneNotConnected.png")
    not_operational = dpg.load_image("src/dronesImg/droneNotOperational.png")
    

    
    #Crea l'interfaccia
    def __init__(self):
        '''Crea il contesto e il viewport.'''
        dpg.create_context()
        dpg.create_viewport(title='Presentazione droNet', width=800, height=600, min_width= 800, min_height=600)

        self.LST_VW_HEIGHT   = dpg.get_viewport_height()
        self.LST_VW_WIDTH    = dpg.get_viewport_width()

    def setup(self, team_droni):
        '''Fa il setup di dpg, mostra il viewport, gestice il render loop e distrugge il contesto'''
        dpg.setup_dearpygui()
        dpg.show_viewport()

        #imposta ogni quanto ripetere il render loop allo stesso valore del refresh rate
        dpg.set_viewport_vsync(True)
        #per ogni frame (basato sul refresh rate del monitor) effettua un'azione (se c'è il render loop va tolto il start_dearpygui())
        while dpg.is_dearpygui_running():
            if self.LST_VW_WIDTH != dpg.get_viewport_width() or self.LST_VW_HEIGHT != dpg.get_viewport_height():
                self.LST_VW_WIDTH    = dpg.get_viewport_width()
                self.LST_VW_HEIGHT   = dpg.get_viewport_height()

                dpg.configure_item(item= "mapContainer", width= self.LST_VW_WIDTH-200, height= self.LST_VW_HEIGHT)
                dpg.configure_item(item= "sidebar", width= 200, height= self.LST_VW_HEIGHT, pos= (self.LST_VW_WIDTH-dpg.get_item_width("sidebar"), 0))

                #roba mappa se MATTEO vuole guardare
                #dpg.configure_item(item= self.tags["maps"], width = dpg.get_item_width("mapContainer"), height = dpg.get_item_height("mapContainer"))
            
            updated_copy = team_droni.updated.copy()
            team_droni.updated = []
            for id in updated_copy:
                if not dpg.does_alias_exist("drone"+str(id)):
                    with dpg.group(label= "Drone", filter_key= str(id), parent= "sideBarFilter"):    
                        with dpg.group(label= "header", width= 80, horizontal= True, horizontal_spacing= 20):
                            dpg.add_text("Drone "+ str(id))
                            dpg.add_button(callback= UI.info_drone, user_data= [team_droni.ids[id]], label= "Info")
                        with dpg.drawlist(width= 170, height= 170, tag= "drone" + str(id)):
                            if team_droni.ids[id].stato == Stato.CONNECTED:
                                dpg.draw_image("connected", pmin= (0,0), pmax= (170, 170))
                            elif team_droni.ids[id].stato == Stato.NOT_CONNECTED:
                                dpg.draw_image("not_connected", pmin= (0,0), pmax= (170, 170))
                            else:
                                dpg.draw_image("not_operational", pmin= (0,0), pmax= (170, 170))
                else:
                    dpg.delete_item(dpg.get_item_children("drone"+str(id), 0))
                    if team_droni.ids[id].stato == Stato.CONNECTED:
                        dpg.draw_image("connected", pmin= (0,0), pmax= (170, 170), parent= "drone"+str(id))
                    elif team_droni.ids[id].stato == Stato.NOT_CONNECTED:
                        dpg.draw_image("not_connected", pmin= (0,0), pmax= (170, 170), parent= "drone"+str(id))
                    else:
                        dpg.draw_image("not_operational", pmin= (0,0), pmax= (170, 170), parent= "drone"+str(id))

            dpg.render_dearpygui_frame()
            
        dpg.destroy_context()

    def interface(self):
        '''Funzione che definisce l'interfaccia'''

        with dpg.value_registry(label= "Registro valori", tag = "baseValues", user_data= ("valore1", 2, "valore3")):
            dpg.add_string_value(default_value= "Stringa di dafault", tag="defString")

        with dpg.texture_registry():
            dpg.add_static_texture(width= self.connected[0], height= self.connected[1], default_value= self.connected[3], tag= "connected")
            dpg.add_static_texture(width= self.not_connected[0], height= self.not_connected[1], default_value= self.not_connected[3], tag= "not_connected")
            dpg.add_static_texture(width= self.not_operational[0], height= self.not_operational[1], default_value= self.not_operational[3], tag= "not_operational")

        with dpg.window(width=600, height=600, tag= "mapContainer", label= "Mappa", no_title_bar= True, no_move = True, no_resize= True):
            #cose mappa se MATTEO vuole guardare
            """ self.tags["maps"] = map.add_map_widget(width= self.screenSize[0]-200, height= self.screenSize[1], center= (41.890210, 12.492231), zoom_level= 12)
            #da finire """


        with dpg.window(tag="sidebar", label= "Sidebar - Lista droni", pos= (600, 0), no_move = True, no_resize= True, no_title_bar= True, width= 200, height= 600):
            dpg.add_input_text(hint= "Cerca droni", callback= UI.sideBarFilterCallback)
            dpg.add_filter_set(tag = "sideBarFilter")

    #callback functions
    def info_drone(sender, app_data, user_data):
        with dpg.window(width=500, height=300, tag= "infoDrone", label= "Info drone", modal= True):
            '''NOTA: il tag dentro ad un evento che può accadere più volte causerà errore dopo la prima volta
                    occorre quindi effettuare una remove_alias() alla fine della funzione'''
            dpg.add_text("ID: " + str(user_data[0].id))
            dpg.add_text("Stato: " + str(user_data[0].stato.value))
            dpg.add_text("Posizione: " + str(user_data[0].posizione))
            dpg.add_text("Batteria: " + str(user_data[0].batteria) + "%")
            dpg.add_text("Obbiettivo: " + str(user_data[0].obbiettivo))
        dpg.remove_alias("infoDrone")

    def sideBarFilterCallback(sender, filter):
        dpg.set_value("sideBarFilter", filter)

interface = UI()
interface.interface()

team = TeamDroni()

interface.setup(team)