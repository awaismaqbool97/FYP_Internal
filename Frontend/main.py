import customtkinter as ctk
import tkinter as tk
from PIL import Image
import cv2

from UI.Homepage import Homepage
from UI.Controller import Controller
from UI.Autonomous import Autonomous_Movement
from UI.Footer import create_footer
from PIL import Image, ImageTk
from threading import Timer
from djitellopy import Tello
import threading
from time import sleep


tello = Tello()


# Create Main Frame (child of Root)
def create_main_frame(parent):
    main_frame = ctk.CTkFrame(master=parent)
    main_frame.configure(fg_color="#86B6F6")
    main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    main_frame.grid_rowconfigure(0,weight=1)
    main_frame.grid_columnconfigure(0,weight=1)

    tab_view = MyTabView(master=main_frame)
    tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    tab_view.configure(fg_color="#B4D4FF")

    return main_frame



# Create Tabs (Child of Main Frame)
class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create tabs
        self.add("Home")
        self.add("Drone Controller")
        self.add("Autonomous Movement") 

        Homepage(self.tab("Home")) # (UI/homepage.py)
        Controller(self.tab("Drone Controller"),tello) # (UI/Controller.py)
        Autonomous_Movement(self.tab("Autonomous Movement"),tello) # (UI/Autonomous.py)





def main():
    root = ctk.CTk()
    root.title("Autonomous Surveillance Drone")
    root.geometry("1200x500")
    root.configure(fg_color="#176B87")
    root.maxsize(1920,1080)
    root.minsize(1500,700)

    create_main_frame(root)
    # Footer ( Child of Root ) ( Code in UI/Footer.py )
    create_footer(root,tello)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
