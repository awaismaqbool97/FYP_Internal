import customtkinter as ctk
from PIL import Image


# First Tab
def Homepage(parent):
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)
    home_frame = ctk.CTkFrame(master=parent) #, border_width=5, border_color="black"
    home_frame.configure(fg_color="#EEF5FF")
    home_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    label1 = ctk.CTkLabel(home_frame, text="Final Year Project", font=("Arial", 30))
    label1.grid(row=0, column=0,columnspan=2 ,sticky="n", pady= 5)

    label2 = ctk.CTkLabel(home_frame, text="24-FYP-111", font=("Arial", 20))
    label2.grid(row=1, column=0,columnspan=2 ,sticky="n", pady = 1)

    label3 = ctk.CTkLabel(home_frame, text="Muhammad Awais", font=("Arial", 20))
    label3.grid(row=2, column=0, sticky="e", padx = 10)

    label4 = ctk.CTkLabel(home_frame, text="Kashif Mahmood", font=("Arial", 20))
    label4.grid(row=2, column=1, sticky="w", padx = 10)

    image2 = ctk.CTkImage(light_image=Image.open("Resources/home.jpg"),dark_image=Image.open("Resources/home.jpg"), size=(500,400))
    image_label = ctk.CTkLabel(home_frame, image=image2, text="FYP Project", padx = 10, pady = 10) 
    image_label.grid(row=3,column=0, columnspan=2, sticky= "n")

    label5 = ctk.CTkLabel(home_frame, text="Supervisor: Mr. Nasir Mahmood\nCo-Supervisor: Dr. Muhammad Asif",justify="left" ,font=("Arial", 20))
    label5.grid(row=4, column=0,columnspan=2, sticky="ew", padx = 10)


    home_frame.grid_columnconfigure((0,1), weight=1)
