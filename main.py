import dearpygui.dearpygui as dpg
from screeninfo import get_monitors

monitor = get_monitors()[0]  # primary

dpg.create_context()
dpg.create_viewport(title="Deimos",width=monitor.width,height=monitor.height)#small_icon="Iamgui/demand.png",large_icon="Iamgui/demand.png")

def callback(sender, app_data):
    print('OK was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)

def savefile(sender, app_data):
    text_content = dpg.get_value("Box")

    file_path = app_data['file_path_name'] + '.txt'

    try:
        with open(file_path, 'w') as file:
            file.write(text_content)
        print(f"File saved to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
def openfile(sender, app_data):
    filepath = app_data['file_path_name']


    try:
        with open(filepath, 'r') as file:
            content = file.read()
        dpg.set_value("Box", content)
    except Exception as e:
        dpg.set_value("Box", "Error opening file")
        print(f"Error opening file: {e}")

def cancel_callback(sender, app_data):
    print('Cancel was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)

#Get Window Size there is another way to do this with dpg.get_viewport_client_witdh()
def get_viewport_size():
    widthbox = dpg.get_viewport_client_width()
    heightbox = dpg.get_viewport_client_height()
    return widthbox, heightbox

def print_me(sender):   
    print(f"Menu Item: {sender}")

dpg.add_file_dialog(directory_selector=False, show=False, callback=savefile, tag="file_dialog_id",cancel_callback=cancel_callback, width=700 ,height=400,default_filename="untitled")

with dpg.file_dialog(directory_selector=False, show=False, callback=openfile, tag="openfile",cancel_callback=cancel_callback, width=700 ,height=400,default_filename="untitled"):
    dpg.add_file_extension(".*")
    dpg.add_file_extension(".txt", color=(255, 255, 0, 255), custom_text="[text]")
    #dpg.add_file_extension("", color=(150, 255, 150, 255))
    #dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
    #dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
    dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")



def program():
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save",callback=lambda: dpg.show_item("file_dialog_id"))
            #TODO dpg.add_menu_item(label="Save As", callback=print_me)
            dpg.add_menu_item(label="Open", callback=lambda: dpg.show_item("openfile"))
        #TODO with dpg.menu(label="Settings"):
        #     dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
        #     dpg.add_menu_item(label="Setting 2", callback=print_me)
        #     dpg.add_menu_item(label="Help", callback=print_me)
        with dpg.menu(label="Widget Items"):
            dpg.add_checkbox(label="Pick Me", callback=print_me)
            dpg.add_button(label="Press Me", callback=print_me)
            dpg.add_color_picker(label="Color Me", callback=print_me)
    dpg.add_input_text(tag="Box",multiline=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height())
    

# dpg.add_file_dialog(
#     directory_selector=True, show=False, callback=callback, tag="file_dialog_id",
#     cancel_callback=cancel_callback, width=700 ,height=400)

#Actual Window to be created
with dpg.window(tag="main"):
    
    program()


#Necessary to run the program
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("main",True)

while dpg.is_dearpygui_running():
    widthbox, heightbox = get_viewport_size()
    dpg.set_item_width("Box", widthbox)
    dpg.set_item_height("Box", heightbox)

    dpg.render_dearpygui_frame()

    
dpg.destroy_context()








