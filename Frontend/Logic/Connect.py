from time import sleep

from Logic.Getvideo import update_video_stream
import config
import threading


# Periodically Checks connection with Drone and updates relative messages
def Connect(tello, connection_label,battery_label):

    while True:
        # if not config.moving_trace:
            connection_response = tello.send_command_with_return("command",timeout=3)

            if connection_response == "ok":
                tello.streamon() # start streaming from drone
                config.connection_text = "Drone connected"
                connection_label.configure(text=config.connection_text,text_color="black")

                # Call update_video_stream once
                if not config.terminate_stream:
                    # video_thread1 = threading.Thread(target=update_video_stream,args=(config.stream_label1,tello))
                    # video_thread2 = threading.Thread(target=update_video_stream,args=(config.stream_label2,tello))
                    # video_thread1.start()
                    # video_thread2.start()
                    update_video_stream(config.stream_label1, tello)
                    update_video_stream(config.stream_label2, tello)

                # Periodically check for response changes
                while True:
                    if not config.moving_trace:
                        new_response = tello.send_command_with_return("command")
                        battery = tello.get_battery()
                        battery_label.configure(text=f"Battery Percentage: {battery} %")
                        if new_response != "ok":
                            break  # Exit inner loop if response changes
                    sleep(3)

                config.terminate_stream = True # Set to True, so update_video_stream will never be called again until Progrm is running
                config.connection_text = "Drone disconnected"
                connection_label.configure(text=config.connection_text,text_color="red")
                sleep(1)

            else:
                config.connection_text = "Drone Failed to Connect"
                connection_label.configure(text=config.connection_text,text_color="red")
                sleep(1)

