import dearpygui.dearpygui as dpg

dpg.create_context()

def callback1(sender, stringa):
    if dpg.does_alias_exist("filter_id"):
        dpg.delete_item("filter_id")
    if dpg.get_value("searchBar") != '':
        with dpg.filter_set(id="filter_id", parent= "search"):
            dpg.add_text("aaa1.c",
                         filter_key="aaa1.c", bullet=True)
            dpg.add_text("bbb1.c",
                         filter_key="bbb1.c", bullet=True)
            dpg.add_text("ccc1.c",
                         filter_key="ccc1.c", bullet=True)
            dpg.add_text("aaa2.cpp",
                         filter_key="aaa2.cpp", bullet=True)
            dpg.add_text("bbb2.cpp",
                         filter_key="bbb2.cpp", bullet=True)
            dpg.add_text("ccc2.cpp",
                         filter_key="ccc2.cpp", bullet=True)
            dpg.add_text("abc.h",
                         filter_key="abc.h", bullet=True)
            dpg.add_text("hello, world",
                         filter_key="hello, world", bullet=True)
        dpg.set_value("filter_id", stringa)


with dpg.window(label="about", width =500,
                height=300, tag= "search"):
    dpg.add_input_text(label="Filter (inc, -exc)",
                       callback=callback1, tag = "searchBar")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()