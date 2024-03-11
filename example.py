import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from time import time


def demo_example():
    dpg.create_context()
    dpg.create_viewport(title = 'Custom Title', width = 600, height = 600)

    demo.show_demo()

    dpg.setup_dearpygui()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def viewport_example():
    dpg.create_context()

    with dpg.window(label = "Example Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label = "Save")
        dpg.add_input_text(label = "string", default_value = "Quick brown fox")
        dpg.add_slider_float(label = "float", default_value = 0.273, max_value = 1)

    with dpg.window(label = "test"):
        dpg.add_text("THOMAS SCEMO")
        dpg.add_button(label = "PURE FROCIO",callback = lambda : print("TRUE"))

    dpg.create_viewport(title = 'Custom Title', width = 600, height = 200)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def render_loop_example():
    dpg.create_context()

    with dpg.window(label = "Example Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label = "Save")
        dpg.add_input_text(label = "string", default_value = "Quick brown fox")
        dpg.add_slider_float(label = "float", default_value = 0.273, max_value = 1)

    dpg.create_viewport(title = 'Custom Title', width = 600, height = 200)
    dpg.setup_dearpygui()
    dpg.show_viewport()

    start = 0
    # below replaces, start_dearpygui()
    while dpg.is_dearpygui_running():
        now = time()
        # insert here any code you would like to run in the render loop
        # you can manually stop by using stop_dearpygui()
        print(f"delta = {(now - start)}s")
        start = now
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


def primary_window_example():
    dpg.create_context()

    with dpg.window(tag = "Primary Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label = "Save")
        dpg.add_input_text(label = "string", default_value = "Quick brown fox")
        dpg.add_slider_float(label = "float", default_value = 0.273, max_value = 1)

    with dpg.window(tag = "Second"):
        dpg.add_button(label = "DAJE", callback = lambda: print("EHEH"))
        dpg.add_text("OIA")

    dpg.create_viewport(title = 'Custom Title', width = 600, height = 200)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


def tags_example():
    dpg.create_context()

    with dpg.window(label = "Tutorial"):
        b0 = dpg.add_button(label = "button 0")
        b1 = dpg.add_button(tag = 100, label = "Button 1")
        dpg.add_button(tag = "Btn2", label = "Button 2")

    print(b0)
    print(b1)
    print(dpg.get_item_label("Btn2"))

    dpg.create_viewport(title = 'Custom Title', width = 600, height = 200)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def container_example():
    import dearpygui.dearpygui as dpg

    dpg.create_context()

    with dpg.window(label = "Tutorial"):
        dpg.add_button(label = "Button 1")
        dpg.add_button(label = "Button 2")
        with dpg.group():
            dpg.add_button(label = "Button 3")
            dpg.add_button(label = "Button 4")
            with dpg.group() as group1:
                pass
    dpg.add_button(label = "Button 6", parent = group1)
    dpg.add_button(label = "Button 5", parent = group1)

    dpg.create_viewport(title = 'Custom Title', width = 600, height = 400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def configuration_example():

    dpg.create_context()

    with dpg.window(label = "Tutorial"):
        # configuration set when button is created
        dpg.add_button(label = "Apply", width = 300)

        # user data and callback set any time after button has been created
        btn = dpg.add_button(label = "Apply 2")
        dpg.set_item_label(btn, "Button 57")
        dpg.set_item_width(btn, 200)

    dpg.show_item_registry()

    dpg.create_viewport(title = 'Custom Title', width = 800, height = 600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def callback_example():
    import dearpygui.dearpygui as dpg

    dpg.create_context()

    def button_callback(sender, app_data, user_data):
        print(f"sender is: {sender}")
        print(f"app_data is: {app_data}")
        print(f"user_data is: {user_data}")

    with dpg.window(label = "Tutorial"):
        # user data and callback set when button is created
        dpg.add_button(label = "Apply", callback = button_callback, user_data = "Some Data")

        # user data and callback set any time after button has been created
        btn = dpg.add_button(label = "Apply 2", )
        dpg.set_item_callback(btn, button_callback)
        dpg.set_item_user_data(btn, "Some Extra User Data")

    dpg.create_viewport(title = 'Custom Title', width = 800, height = 600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def value_example():
    dpg.create_context()

    def print_value(sender):
        print(dpg.get_value(sender))

    with dpg.window(width = 300):
        input_txt1 = dpg.add_input_text()
        # The value for input_text2 will have a starting value
        # of "This is a default value!"
        input_txt2 = dpg.add_input_text(
            label = "InputTxt2",
            default_value = "This is a default value!",
            callback = print_value
        )

        slider_float1 = dpg.add_slider_float()
        # The slider for slider_float2 will have a starting value
        # of 50.0.
        slider_float2 = dpg.add_slider_float(
            label = "SliderFloat2",
            default_value = 50.0,
            callback = print_value
        )

        dpg.set_item_callback(input_txt1, print_value)
        dpg.set_item_callback(slider_float1, print_value)

        print(dpg.get_value(input_txt1))
        print(dpg.get_value(input_txt2))
        print(dpg.get_value(slider_float1))
        print(dpg.get_value(slider_float2))

    dpg.create_viewport(title = 'Custom Title', width = 800, height = 600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def handler_example():
    import dearpygui.dearpygui as dpg

    dpg.create_context()

    def change_text(sender, app_data):
        dpg.set_value("text item", f"Mouse Button ID: {app_data}")

    with dpg.window(width = 500, height = 300):
        dpg.add_text("Click me with any mouse button", tag = "text item")
        with dpg.item_handler_registry(tag = "widget handler"):
            dpg.add_item_clicked_handler(callback = change_text)
        dpg.bind_item_handler_registry("text item", "widget handler")

    dpg.create_viewport(title = 'Custom Title', width = 800, height = 600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def esplodi():
    dpg.create_context()

    dpg.show_documentation()
    dpg.show_style_editor()
    dpg.show_debug()
    dpg.show_about()
    dpg.show_metrics()
    dpg.show_font_manager()
    dpg.show_item_registry()

    dpg.create_viewport(title = 'Custom Title', width = 800, height = 600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    demo_example()
    # viewport_example()
    # render_loop_example()
    # primary_window_example()
    # tags_example()
    # container_example()
    # configuration_example()
    # callback_example()
    # value_example()
    # handler_example()
    # esplodi()
    dpg.create_context()
    dpg.create_viewport(title = 'Custom Title', width = 600, height = 600)

    # demo.show_demo()

    dpg.show_metrics()
    dpg.set_viewport_vsync(False)

    dpg.setup_dearpygui()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
