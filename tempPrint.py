from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:
    t = sense.get_temperature()


    t = round(t, 1)

    print(t)

    sleep(1.0)
