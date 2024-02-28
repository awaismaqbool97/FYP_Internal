import cv2
from PIL import Image, ImageTk
import config

video_writer = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (800, 600))

def update_video_stream(image_label, tello):
        frame = tello.get_frame_read().frame
        config.stream_label1.configure(text="Live streaming")
        config.stream_label2.configure(text="Live streaming")
        frame = cv2.resize(frame, (800, 600))  # Resize frame to fit in the frame
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert frame colors from BGR to RGB
        video_writer.write(frame) 
        img = Image.fromarray(frame)  # Convert OpenCV frame to PIL Image
        img_tk = ImageTk.PhotoImage(image=img)  # Convert PIL Image to Tkinter-compatible image
        image_label.img_tk = img_tk  # Prevent garbage collection
        image_label.configure(image=img_tk)  # Update image in label
        image_label.after(10, lambda: update_video_stream(image_label, tello))