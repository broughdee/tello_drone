from djitellopy import tello
from time import sleep

t = tello.Tello()
t.connect()
print(t.get_battery())

# take off + adjust to correct height (200cm)
t.takeoff()
t.move_up(120)

# move + turn + move to necessary area
t.move_forward(500)
t.move_forward(100)
sleep(.5)
t.rotate_counter_clockwise(90)
sleep(.5)
t.move_forward(300)
sleep(.5)

#celebrate
t.rotate_clockwise(540)
t.move_up(50)
t.move_down(75)
t.move_up(15)
t.rotate_clockwise(90)

#return
sleep(.5)
t.move_forward(500)
t.move_forward(100)
sleep(.5)
t.rotate_counter_clockwise(90)
sleep(.5)
t.move_forward(300)
sleep(.5)
t.rotate_counter_clockwise(90)

#land
t.land()
