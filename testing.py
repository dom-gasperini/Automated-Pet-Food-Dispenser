from datetime import datetime
import threading

def print_message():
    print("hello there!")


t = threading.Timer(3, print_message())
t.start()

i = 0

while True:
    i += 1


"""
current_time = datetime.now()

current_time = current_time.strftime("%H:%M")

print(current_time)

test_time1 = "12:00"
test_time2 = "15:12"

if current_time == test_time1:
    print(True)
else:
    print(False)


if current_time == test_time2:
    print(True)
else:
    print(False)
"""
