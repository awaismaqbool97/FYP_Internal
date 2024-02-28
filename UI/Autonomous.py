import customtkinter as ctk
import threading
from PIL import Image
from Logic.Move import move_xyz
import config


# Called when Move button pressed on Autonomous Page
def start_move(entry_x, entry_y, entry_z, error_label, tello):

    # Checking Input cannot be empty/non-int
    try:
        if entry_x.get() == "":
            error_label.configure(text="X cannot be empty", state="normal")
            return
        if entry_y.get() == "":
            error_label.configure(text="Y cannot be empty", state="normal")
            return
        if entry_z.get() == "":
            error_label.configure(text="Z cannot be empty", state="normal")
            return
        
        try:
            int(entry_x.get())
        except:
            error_label.configure(text="X is not Int", state="normal")
            return
        
        try:
            int(entry_y.get())
        except:
            error_label.configure(text="Y is not Int", state="normal")
            return
        
        try:
            int(entry_x.get())
        except:
            error_label.configure(text="Z is not Int", state="normal")
            return

       
        config.moving_trace = True

        x = int(entry_x.get())
        y = int(entry_y.get())
        z = int(entry_z.get())

        #Create separate Thread for drone's autonomous movement using coordinates x,y,z
        move_thread = threading.Thread(target=move_xyz,args=(x,y,z,tello))
        move_thread.start()
        
        error_label.configure(text="", state="disabled")
    except Exception as e:
        # Handle any exceptions that occur during movement
        error_label.configure(text=str(e), state="normal")


# Third Tab
def Autonomous_Movement(parent,tello):

    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)
    home_frame = ctk.CTkFrame(master=parent) #, border_width=5, border_color="black"
    home_frame.configure(fg_color="#EEF5FF")
    home_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    label1 = ctk.CTkLabel(home_frame, text="Drone Autonomously Moves", font=("Arial", 30))
    label1.grid(row=0, column=0,columnspan=2 ,sticky="n", pady= 5)

    label2 = ctk.CTkLabel(home_frame, text="Write Coordinates:", font=("Arial", 20))
    label2.grid(row=1, column=0 ,sticky="w", pady =10, padx=140)


    label3 = ctk.CTkLabel(home_frame, text="X-Coordinate:", font=("Arial", 20, "bold"))
    label3.grid(row=2, column=0, sticky="w", padx=10,pady=5)

    entry_x = ctk.CTkEntry(home_frame, placeholder_text="Enter x Coordinate", placeholder_text_color="black")
    entry_x.grid(row=3, column=0 ,sticky="w", padx=40,pady=5)

    
    x_value = ctk.CTkLabel(home_frame, text="- Value range is (-500 - 500) cm", font=("Arial", 12))
    x_value.grid(row=4, column=0, sticky="w", padx=10)
    
    
    label4 = ctk.CTkLabel(home_frame, text="Y-Coordinate:", font=("Arial", 20, "bold"))
    label4.grid(row=5, column=0, sticky="w", padx=10,pady=5)

    entry_y = ctk.CTkEntry(home_frame, placeholder_text="Enter y Coordinate", placeholder_text_color="black")
    entry_y.grid(row=6, column=0 ,sticky="w", padx=40,pady=5)

    y_value = ctk.CTkLabel(home_frame, text="- Value range is (-500 - 500) cm", font=("Arial", 12))
    y_value.grid(row=7, column=0, sticky="w", padx=10)

    label4 = ctk.CTkLabel(home_frame, text="Z-Coordinate:", font=("Arial", 20, "bold"))
    label4.grid(row=8, column=0, sticky="w", padx=10,pady=5)

    entry_z = ctk.CTkEntry(home_frame, placeholder_text="Enter z Coordinate", placeholder_text_color="black")
    entry_z.grid(row=9, column=0 ,sticky="w", padx=40,pady=5)

    z_value = ctk.CTkLabel(home_frame, text="- Value range is (-500 - 500) cm", font=("Arial", 12))
    z_value.grid(row=10, column=0, sticky="w", padx=10)


    error_label = ctk.CTkLabel(home_frame, text="Error_Label", font=("Arial", 10, "bold"), text_color="red")
    error_label.grid(row=11, column=0, sticky="w", padx=10,pady=5)

    

    error_label.configure(text="", state="disabled")

    
    # Press to move the drone
    button = ctk.CTkButton(home_frame, text="Move", command=lambda: start_move(entry_x,entry_y,entry_z,error_label,tello))
    button.grid(row=12, column=0 ,sticky="w", padx=270,pady=40)


    image2 = ctk.CTkImage(light_image=Image.open("Resources/home.jpg"),dark_image=Image.open("Resources/home.jpg"))
    config.stream_label2 = ctk.CTkLabel(home_frame, image=image2, text="No streaming", padx = 10, pady = 40) 
    config.stream_label2.grid(row=1,column=1,rowspan=13 ,sticky= "n")
    


    home_frame.grid_columnconfigure((0,1), weight=1)
    home_frame.grid_rowconfigure((10,11,12,13), weight=1)