import time
import keyboard

S = 60
FPS = 120

class FrontEnd(object):
    """ Maintains the Tello display and moves it through the keyboard keys.
        The controls are:
            - T: Takeoff
            - L: Land
            - Arrow keys: Forward, backward, left and right.
            - W and S: Up and down.
            - A and D: Counter clockwise and clockwise rotations (yaw)
    """

    def __init__(self, tello,stop_event):
        self.tello = tello
        self.stop_event = stop_event

        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 10

        self.send_rc_control = False

    def run(self):
        # self.tello.connect()
        # self.tello.set_speed(self.speed)
        # self.tello.streamoff()
        # self.tello.streamon()

        should_stop = False
        while not should_stop and not self.stop_event.is_set():
            self.update()
            time.sleep(1 / FPS)

        # self.tello.end()

    def update(self):
        if keyboard.is_pressed('t'):
            self.tello.takeoff()
            time.sleep(2)
            self.send_rc_control = True
        elif keyboard.is_pressed('l'):
            self.tello.land()
            time.sleep(2)
            self.send_rc_control = False
        elif keyboard.is_pressed('w'):
            self.up_down_velocity = S
        elif keyboard.is_pressed('s'):
            self.up_down_velocity = -S
        elif keyboard.is_pressed('a'):
            self.yaw_velocity = -S
        elif keyboard.is_pressed('d'):
            self.yaw_velocity = S
        elif keyboard.is_pressed('up'):
            self.for_back_velocity = S
        elif keyboard.is_pressed('down'):
            self.for_back_velocity = -S
        elif keyboard.is_pressed('left'):
            self.left_right_velocity = -S
        elif keyboard.is_pressed('right'):
            self.left_right_velocity = S
        else:
            self.for_back_velocity = 0
            self.left_right_velocity = 0
            self.up_down_velocity = 0
            self.yaw_velocity = 0

        if self.send_rc_control:
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity,
                                       self.up_down_velocity, self.yaw_velocity)

def mainn(tello,stop_event):
    frontend = FrontEnd(tello,stop_event)
    frontend.run()

