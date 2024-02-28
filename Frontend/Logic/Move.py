import time
import config
def move_xyz(x,y,z,tello):

    
    tello.takeoff()
    time.sleep(3)

    tello.go_xyz_speed(x,y,z,50)
    # time.sleep(3)

    tello.land()
    # time.sleep(2)

    config.moving_trace = False