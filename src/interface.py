import dearpygui.dearpygui as dpg
import dearpygui_map as map
from screeninfo import get_monitors

class UI:
    """Classe che gestisce l'interfaccia utente, mappa compresa"""
    tags = {}
    
    #Crea l'interfaccia
    def createInterface(self):
        dpg.create_context()
    #   1.  ancorare finestre       ---FATTO---
    #   2.  sovrascrivere chisura
    #   3.  Valori: -Batteria
    #               -Lista posizioni per drone

        def info_drone(sender, app_data, user_data):
            with dpg.window(width=500, height=300, tag= "infoDrone", label= "Info drone", modal= True):
                '''NOTA: il tag dentro ad un evento che può accadere più volte causerà errore dopo la prima volta
                        occorre quindi effettuare una remove_alias() alla fine della funzione'''

                dpg.add_text("Informazione drone")
            dpg.configure_item(sender, label = "Sono stato usato")
            print(sender)
            print(app_data)
            print(user_data)

            dpg.remove_alias("infoDrone")

        def sideBarFilterCallback(sender, filter):
            dpg.set_value("sideBarFilter", filter)
        

        screenSize = (get_monitors()[0].width, get_monitors()[0].height)
        width, height, channels, data = dpg.load_image("/home/thomas/Documents/Università/DemoDroni/src/Thomas/droneMQ_9.jpg")

        with dpg.value_registry(label= "Registro valori", tag = "baseValues", user_data= ("valore1", 2, "valore3")):
            dpg.add_string_value(default_value= "Stringa di dafault", tag="defString")

        #with dpg.theme() as connected_theme:
            #non so che cazzo ce va qua (devo trovare delle informazioni su cosa va dentro dpg.theme_component()

        with dpg.texture_registry():
            dpg.add_static_texture( width= width, height= height, default_value= data, tag= "liberta",)

        with dpg.window(width=600, height=600, tag= "mapContainer", label= "Mappa", no_title_bar= True, no_move = True, no_resize= True):
            self.tags["maps"] = map.add_map_widget(width= screenSize[0], height= screenSize[1], center= (41.890210, 12.492231), zoom_level= 12)
            #da finire

        with dpg.window( tag="sidebar", label= "Sidebar - Lista droni", pos= (600, 0), no_move = True, no_resize= True, no_title_bar= True):
            dpg.add_input_text(hint= "Cerca droni", callback=sideBarFilterCallback)
            with dpg.filter_set(tag = "sideBarFilter"):
                for i in range(5):
                    with dpg.group(label= "Drone", filter_key= "Drone " + str(i+1)):
                        with dpg.group(label= "left", width= 80, horizontal= True, horizontal_spacing= 20):
                            dpg.add_text("Drone "+ str(i+1))
                            dpg.add_button(callback=info_drone, user_data= ["ciaone", 1, 2, 3, "basta"], label= "Info")
                        '''with dpg.group(label= "right", width= 80, pos= (100, 100)):
                            dpg.add_button(callback=info_drone, user_data= ["ciaone", 1, 2, 3, "basta"], label= "Info")'''
                        with dpg.drawlist(width= 170, height= 170):
                            dpg.draw_image("liberta", pmin= (0,0), pmax= (179, 179))

        dpg.configure_item(item= "sidebar", width= 200, height= 600)

        dpg.create_viewport(title='Presentazione droNet', width=800, height=600, min_width= dpg.get_item_width("sidebar")+dpg.get_item_width("mapContainer"), min_height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()

        LST_VW_HEIGHT   = dpg.get_viewport_height()
        LST_VW_WIDTH    = dpg.get_viewport_width()

        #imposta ogni quanto ripetere il render loop allo stesso valore del refresh rate
        dpg.set_viewport_vsync(True)
        #per ogni frame (basato sul refresh rate del monitor) effettua un'azione
        while dpg.is_dearpygui_running():
            if LST_VW_WIDTH != dpg.get_viewport_width() or LST_VW_HEIGHT != dpg.get_viewport_height():
                LST_VW_WIDTH    = dpg.get_viewport_width()
                LST_VW_HEIGHT   = dpg.get_viewport_height()

                dpg.configure_item(item= "mapContainer", width= LST_VW_WIDTH-200, height= LST_VW_HEIGHT)
                dpg.configure_item(item= "sidebar", width= 200, height= LST_VW_HEIGHT, pos= (LST_VW_WIDTH-dpg.get_item_width("sidebar"), 0))
                #dpg.configure_item(item= self.tags["maps"], width = dpg.get_item_width("mapContainer"), height = dpg.get_item_height("mapContainer"))
            dpg.render_dearpygui_frame()

        dpg.start_dearpygui()
        dpg.destroy_context()

