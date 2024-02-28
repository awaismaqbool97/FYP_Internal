import customtkinter as ctk


# Variables being used in different files as Global variables for dynamic changes
stream_label1 = ctk.CTkLabel # Video Frame in Controller Page
stream_label2 = ctk.CTkLabel # video Frame in Autonomous Page
terminate_stream = False # Controls stream (will start only once at start of program)
connection_text = "" # Indication Drone connection in Footer
moving_trace = False 