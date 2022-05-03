# the automatic cat food dispenser!

# *** imports *** #
import time
from gpiozero import Servo, LED

# *** defines *** #
MOTOR_PIN = 2

# *** setup GPIO *** #
servo = Servo(MOTOR_PIN)

# main
def main():
	# loop
	while True:
		# open door
		i = 0
		while i < 6:
			servo.min()
			time.sleep(0.25)
			servo.max()
			time.sleep(0.25)
			i = i + 1
		# close door
		servo.max()
		time.sleep(3)

        
# run it
main()
