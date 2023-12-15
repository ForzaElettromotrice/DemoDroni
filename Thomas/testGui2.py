import dearpygui.dearpygui as dpg

"""per comodità nel passare i valori per le callback usiamo sempre le liste []"""

dpg.create_context()

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

with dpg.value_registry(label= "Registro valori", tag = "baseValues", user_data= ("valore1", 2, "valore3")):
    dpg.add_string_value(default_value= "Stringa di dafault", tag="defString")

with dpg.handler_registry():
    dpg.add_mouse_move_handler(callback=change_text)

width, height, channels, data = dpg.load_image("/home/thomas/PycharmProjects/droneNet/droneMQ_9.jpg")

with dpg.texture_registry():
    dpg.add_static_texture( width= width, height= height, default_value= data, tag= "liberta",)

with dpg.window( width=500, height=300, tag= "mappa", label= "Mappa", no_title_bar= True, no_move = True):
    with dpg.menu_bar(label = "menu", tag= "menu"):
        with dpg.menu(label= "Menu 1", tag="menu1"):
            dpg.add_menu_item(label= "Sub menu1")
        dpg.add_button(label= "Impostazioni", tag = "impost", callback= impostWindow, user_data= ["dato 1"])
        print(dpg.get_item_children("menu"))
        print(dpg.get_item_children("mappa"))
        print(dpg.get_alias_id("menu"))
    dpg.add_text("Hover Me!", tag="text item")

with dpg.window(width= 200, height = 500, tag="sidebar", label= "Sidebar - Lista droni", pos= (500, 0), no_move = True, no_collapse= True):
    with dpg.filter_set()
    for i in range(5):
        with dpg.group(label= "Drone", filter_key= "Drone " + str(i+1)):
            with dpg.group(label= "left", width= 80):
                dpg.add_text("Drone "+ str(i+1))
                dpg.add_button(callback=info_drone, user_data= ["ciaone", 1, 2, 3, "basta"], label= "Info")
            '''with dpg.group(label= "right", width= 80, pos= (100, 100)):
                dpg.add_button(callback=info_drone, user_data= ["ciaone", 1, 2, 3, "basta"], label= "Info")'''
            with dpg.drawlist(width= 180, height= 180):
                dpg.draw_image("liberta", pmin= (0,0), pmax= (179, 179))


dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()