import socket
import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

led.init()
switch.init()

def blink_led(delay):
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def main():
    while True:
        count = 0

        while switch.read_slide_switch():
            blink_led(0.1)
        else:
            while switch.read_slide_switch() == 0:
                if count <= 50:
                    blink_led(0.05)
                    count += 1
                else:
                    led.set_output(0, 0)


if __name__ == "__main__":
    main()