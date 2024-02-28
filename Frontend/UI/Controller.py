import customtkinter as ctk
import threading
from PIL import Image
from Logic.Keycontrol import mainn
import config

# Second Tab
def Controller(parent,tello):

    # Variable to track if mainn() is running which is Drone Controller
    running = False 
    stop_event = threading.Event()

    # When Switch on, we can control Drone. When off, Nathi
    def switch_event():
        nonlocal running  
        if switch_var.get() == "on":
            if running==False:
                running = True
                stop_event.clear()
                thread = threading.Thread(target=mainn, args=(tello,stop_event))
                thread.start()
        elif switch_var.get() == "off":
            if running:
                running = False
                stop_event.set()
    

    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)
    home_frame = ctk.CTkFrame(master=parent) #, border_width=5, border_color="black"
    home_frame.configure(fg_color="#EEF5FF")
    home_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    label1 = ctk.CTkLabel(home_frame, text="Maintains the Tello display and moves it through the keyboard keys", font=("Arial", 30))
    label1.grid(row=0, column=0,columnspan=2 ,sticky="n", pady= 5)

    switch_var = ctk.StringVar(value="off")
    switch = ctk.CTkSwitch(home_frame, text="Turn On Controls", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
    
    switch.grid(row=1,column=0,columnspan=2, sticky="n")

    label2 = ctk.CTkLabel(home_frame, text="The Controls are:", font=("Arial", 20))
    label2.grid(row=2, column=0 ,sticky="w", pady =10, padx=120)

    label3 = ctk.CTkLabel(home_frame, text="- T: Takeoff", font=("Arial", 20, "bold"))
    label3.grid(row=3, column=0, sticky="w", padx = 10)

    label4 = ctk.CTkLabel(home_frame, text="- L: Land", font=("Arial", 20, "bold"))
    label4.grid(row=4, column=0, sticky="w", padx = 10)

    label5 = ctk.CTkLabel(home_frame, text="- Arrow keys: Forward, backward, left and right",font=("Arial", 20, "bold"))
    label5.grid(row=5, column=0,sticky="w", padx = 10)

    label6 = ctk.CTkLabel(home_frame, text="- A and D: Counter clockwise and clockwise rotations", font=("Arial", 20, "bold"))
    label6.grid(row=6, column=0,sticky="w", padx = 10)

    label7 = ctk.CTkLabel(home_frame, text="- W and S: Up and down.", font=("Arial", 20, "bold"))
    label7.grid(row=7, column=0,sticky="w", padx = 10)


    # home_frame.grid_columnconfigure((0,1), weight=1)
    # home_frame.grid_rowconfigure((3,4,5,6,7), weight=1)

    image2 = ctk.CTkImage(light_image=Image.open("Resources/home.jpg"),dark_image=Image.open("Resources/home.jpg"))
    config.stream_label1 = ctk.CTkLabel(home_frame, image=image2, text="No stream", padx = 10, pady = 40) 
    config.stream_label1.grid(row=2,column=1,rowspan=9 ,sticky= "n")


    config.stream_label1.grid_rowconfigure(0,weight=1)
    config.stream_label1.grid_columnconfigure(0,weight=1)


    home_frame.grid_columnconfigure((0,1), weight=1)
    home_frame.grid_rowconfigure((8,9), weight=1)