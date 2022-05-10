from djitellopy import tello
from time import sleep

t = tello.Tello()
t.connect()

print(t.get_battery())
print(t.get_barometer())
