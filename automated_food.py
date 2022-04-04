# the automatic cat food dispenser!

# *** imports *** #
import time
import threading
from gpiozero import * 
from datetime import datetime

# *** defines *** #
BUTTON_PIN = int(18)
MOTOR_PIN = int(25)
DOOR_DELAY = int(2)


# *** setup *** #
button = Button(BUTTON_PIN)
servo = Servo(MOTOR_PIN)


# *** global variables *** #
breakfast = "08:00 AM"
lunch = "12:00 PM"
dinner = "6:00 PM"
breakfast_hour = breakfast[0:2]
lunch_hour = lunch[0:2]
dinner_hour = dinner[0:2]


# check the time, return True if it is a time that food should be dispensed
def get_time():
    # get the current time
    current_time = datetime.now()

    # convert to a easier format for comparison
    current_time = current_time.strftime("%H:%M")

    # test the time
    if current_time == breakfast or current_time == lunch or current_time == dinner:
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
    # open the food door
    servo.max()

    # how long will the motor will stay open 
    time.sleep(DOOR_DELAY)

    # close the food door
    servo.mid()


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
        if feeding_time:
            dispense_food()



# run it
main()
