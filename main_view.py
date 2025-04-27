import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Football Management 2025', width=600, height=200)

def view_main():
    with dpg.window(label="Main Window", width=600, height=200):
        dpg.add_text("Welcome to Football Management 2025")
        dpg.add_text("This is a simple text-based football management game.")
        dpg.add_text("You can manage your team, make transfers, and compete in matches.")
        dpg.add_text("Enjoy the game!")
        dpg.add_button(label="Start Game", callback=lambda: print("Game Started!"))
        dpg.add_button(label="Exit", callback=lambda: dpg.stop_dearpygui())
        dpg.add_button(label="Settings", callback=lambda: print("Settings Opened!"))
        dpg.add_button(label="Help", callback=lambda: print("Help Opened!"))
        dpg.add_button(label="About", callback=lambda: print("About Opened!"))


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
dpg.destroy_viewport()


    