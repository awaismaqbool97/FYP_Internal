
import customtkinter as ctk
import threading
from Logic.Connect import Connect

# Creates Footer ( child of Root )
def create_footer(parent,tello):
    footer_frame = ctk.CTkFrame(master=parent)
    footer_frame.grid(row=1,column=0,sticky="nsew")
    footer_frame.configure(fg_color="#86B6F6")

    footer_label = ctk.CTkLabel(footer_frame, text="DJI Tello Done", height=10, font=("Arial", 20),anchor='center', corner_radius=20) 
    footer_label.grid(row=0, column=0, sticky='w', ipady=10)

    connection_label = ctk.CTkLabel(footer_frame,text="Connecting....", height=10, font=("Arial", 20),anchor='center', corner_radius=20,text_color="red")
    connection_label.grid(row=0,column=1,sticky="nsew")

    battery_label = ctk.CTkLabel(footer_frame,text="Battery Percentage", height=10, font=("Arial", 15),anchor='center', corner_radius=20,text_color="red")
    battery_label.grid(row=0,column=2,sticky="e")
    
    # Thread for Connection Keeps running in while Loop checking Connection with Drone
    thread1 = threading.Thread(target=Connect, args=(tello,connection_label,battery_label))
    thread1.setDaemon(True)
    thread1.start()
    
    footer_frame.grid_rowconfigure(0,weight=1)
    footer_frame.grid_columnconfigure((0,1,2),weight=1)