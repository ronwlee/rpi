from sense_hat import SenseHat
from time import sleep

while True:
    sense = SenseHat()
    sense.clear()

    temp = sense.get_temperature_from_pressure()
    print(temp)
    sleep(5)
