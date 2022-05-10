from djitellopy import tello
from time import sleep

t = tello.Tello()
t.connect()

print(t.get_battery())

t.takeoff()
t.flip_left()
t.rotate_clockwise(360)
t.flip_right()
t.move_up()
t.land()
