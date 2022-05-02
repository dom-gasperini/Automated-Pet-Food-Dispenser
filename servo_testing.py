# the automatic cat food dispenser!

# *** imports *** #
import time
from gpiozero import Button, Servo
from datetime import datetime

# *** defines *** #
BUTTON_PIN = int(18)
MOTOR_PIN = int(25)
DOOR_DELAY = int(2)


# *** setup GPIO *** #
button = Button(BUTTON_PIN)
servo = Servo(MOTOR_PIN)


# dispense the food
def dispense_food():
    # open the food door
    servo.max()

    # how long will the motor will stay open in seconds
    time.sleep(DOOR_DELAY)

    # close the food door
    servo.mid()


# main
def main():
    # loop
    while True:
        # turn servo
        dispense_food()

        # delay
        time.sleep(3)

        
# run it
main()
