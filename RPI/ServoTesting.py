from gpiozero import Servo, PWMOutputDevice
from time import sleep
servo = Servo(4,min_pulse_width=0.001, max_pulse_wisdth=0.002,frame_width=0.0025)



# Rotate servo to extremes 10 times
for j in range(10):
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)

# send servo to pos 0
servo.value = 0