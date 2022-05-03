# the automatic cat food dispenser!

# *** imports *** #
import time
import threading
from gpiozero import Button, Servo
from datetime import datetime

# *** defines *** #
BUTTON_PIN = 3
MOTOR_PIN = 2
DOOR_DELAY = 0.25
BREAKFAST = "08:00 AM"
LUNCH = "12:00 PM"
DINNER = "06:00 PM"


# *** setup GPIO *** #
button = Button(BUTTON_PIN)
servo = Servo(MOTOR_PIN)


# *** global variables *** #
breakfast_hour = BREAKFAST[0:2]
lunch_hour = LUNCH[0:2]
dinner_hour = DINNER[0:2]


# check the time, return True if it is a time that food should be dispensed
def get_time():
    # get the current time
    current_time = datetime.now()

    # convert to a easier format for comparison
    current_time = current_time.strftime("%H:%M")

    # test the time
    if current_time == BREAKFAST or current_time == LUNCH or current_time == DINNER:
        # start interrupt timer for the next get_time() call
        timer = threading.Timer(30, get_time())
        timer.start()        
        # return True if it's time for food
        return True

    # start interrupt timer for the next get_time() call
    timer = threading.Timer(30, get_time())
    timer.start()
    return False


# dispense the food
def dispense_food():
    for i in range(0, 6):
        # open the food door
        servo.max()

        # how long will the motor will stay open in seconds
        time.sleep(DOOR_DELAY)

        # close the food door
        servo.min()

        time.sleep(DOOR_DELAY)
    
    # close the door
    servo.min()


# main
def main():
    # loop
    while True:
        # check for button press DEPENDS IF PULLED HIGH OR LOW!!!!!!!!!
        if button.is_active():
            dispense_food()
        
        # call get_time() & start the interrupt
        feeding_time = get_time()

        # dispense food
        #if feeding_time:
        dispense_food()

        # delay
        time.sleep(10)



# run it
main()
