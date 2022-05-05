# servo testing!

# *** imports *** #
import time
from gpiozero import Servo

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
		for i in range(0, 6):
			servo.min()
			time.sleep(0.25)
			servo.max()
			time.sleep(0.25)

		# close door
		servo.max()
		time.sleep(3)

        
# run it
main()
