import dearpygui.dearpygui as dpg

"""per comodità nel passare i valori per le callback usiamo sempre le liste []"""

dpg.create_context()
#   1.  ancorare finestre       ---FATTO---
#   2.  sovrascrivere chisura


def change_text(sender, app_data):
    if dpg.is_item_hovered("text item"):
        dpg.set_value("text item", f"Stop Hovering Me, Go away!!")
    else:
        dpg.set_value("text item", f"Hover Me!")

def slide_up(sender, app_data, user_data):
    print(user_data)
    dpg.move_item_up(user_data[0])
    dpg.configure_item(sender, label= "Porto giù il mio menu", callback= slide_down,
                       user_data= [user_data[0]])

def slide_down(sender, app_data, user_data):
    print(user_data)
    dpg.move_item_down(user_data[0])
    dpg.configure_item(sender, label="Porto su il mio menu", callback=slide_up,
                       user_data=[user_data[0]])


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


def impostWindow(sender, app_data, user_data):
    with dpg.window(width=500, height=300, tag= "wdwImpostazioni", label= "Impstazioni", modal= True):
        dpg.add_text(source= "defString") #posso usare source definendo un default_value a cui assegniamo un alias
        print(user_data[0])
    dpg.remove_alias("wdwImpostazioni")

def sideBarFilterCallback(sender, filter):
    dpg.set_value("sideBarFilter", filter)

with dpg.value_registry(label= "Registro valori", tag = "baseValues", user_data= ("valore1", 2, "valore3")):
    dpg.add_string_value(default_value= "Stringa di dafault", tag="defString")

with dpg.handler_registry():
    dpg.add_mouse_move_handler(callback=change_text)

#with dpg.theme() as connected_theme:
    #non so che cazzo ce va qua (devo trovare delle informazioni su cosa va dentro dpg.theme_component()

width, height, channels, data = dpg.load_image("/home/thomas/PycharmProjects/droneNet/droneMQ_9.jpg")

with dpg.texture_registry():
    dpg.add_static_texture( width= width, height= height, default_value= data, tag= "liberta",)

with dpg.window(width=500, height=300, tag= "mappa", label= "Mappa", no_title_bar= True, no_move = True, no_resize= True):
    with dpg.menu_bar(label = "menu", tag= "menu"):
        with dpg.menu(label = "Menu 1", tag="menu1"):
            dpg.add_menu_item(label= "Sub menu1")
        dpg.add_button(label= "Impostazioni", tag = "impost", callback= impostWindow, user_data= ["dato 1"])
        print(dpg.get_item_children("menu"))
        print(dpg.get_item_children("mappa"))
        print(dpg.get_alias_id("menu"))
    dpg.add_text("Hover Me!", tag="text item")

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
                with dpg.drawlist(width= 180, height= 180):
                    dpg.draw_image("liberta", pmin= (0,0), pmax= (179, 179))

dpg.configure_item(item= "mappa", width= 600, height= 600)
dpg.configure_item(item= "sidebar", width= 200, height= 600)

dpg.create_viewport(title='Presentazione droNet', width=800, height=600, min_width= dpg.get_item_width("sidebar")+dpg.get_item_width("mappa"), min_height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

LST_VW_HEIGHT   = dpg.get_viewport_height()
LST_VW_WIDTH    = dpg.get_viewport_width()

#imposta ogni quanto ripetere il render loop allo stesso valore del refresh rate
dpg.set_viewport_vsync(True)
#per ogni frame (basato sul refresh rate del monitor) effettua un'azione
while dpg.is_dearpygui_running():
    if LST_VW_WIDTH != dpg.get_viewport_width() or LST_VW_HEIGHT != dpg.get_viewport_height():
        vwWidth = dpg.get_viewport_width()
        vwHeight = dpg.get_viewport_height()

        dpg.configure_item(item= "mappa", width= vwWidth-dpg.get_item_width("sidebar"), height= vwHeight)
        dpg.configure_item(item= "sidebar", width= 200, height= vwHeight, pos= (vwWidth-dpg.get_item_width("sidebar"), 0))
    dpg.render_dearpygui_frame()

dpg.start_dearpygui()
dpg.destroy_context()