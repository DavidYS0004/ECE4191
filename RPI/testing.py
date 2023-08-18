#  Blink an LED with the LGPIO library
#  Uses lgpio library, compatible with kernel 5.11
#  Author: William 'jawn-smith' Wilson

import time
import lgpio
import gpiozero
import multiprocessing
from multiprocessing import Value

# EN_port = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=100) #RAEDM GPIO12
# #ENB_port = gpiozero.OutputDevice(pin=4)

# PWM1_port = gpiozero.DigitalOutputDevice(pin=17, active_high = True,initial_value = True)
# PWM2_port = gpiozero.DigitalOutputDevice(pin=27, active_high = True,initial_value = True)

# encoder = gpiozero.RotaryEncoder(a=21, b=20,max_steps=100000) 
# # Step through duty cycle values, slowly increasing the speed and changing the direction of motion

# encoder.steps = 0
# for j in range(10):
#     EN_port.value = j/10
#     #ENB_port.off() #sets to 0
    
#     #logic PWM1 PWM2 1 0
#     PWM1_port.on()                                                                                                   
#     PWM2_port.off()

#     print('Duty cycle:',EN_port.value,'Direction:',PWM1_port.value, PWM2_port.value)
#     time.sleep(5.0)
#     print('Counter:',encoder.steps,'Speed:',(encoder.steps)/5.0,'steps per second\n')
#     encoder.steps = 0

# EN_port.value =0 

#PWM1 = 17
#PWM2 = 27
#PWMout = 12

# open the gpio chip and set the LED pin as output
#h = lgpio.gpiochip_open(0)
#lgpio.gpio_claim_output(h, PWM1)
#lgpio.gpio_claim_output(h, PWM2)
#lgpio.gpio_claim_output(h, PWMout)

#while True:
#    lgpio.tx_pwm(h,PWMout,500,75)
#    lgpio.gpio_write(h,17,1)
#    lgpio.gpio_write(h,17,0)

#try:
#    while True:
#        # Turn the GPIO pin on
#        lgpio.gpio_write(h, LED, 1)
#        time.sleep(1)#

#        # Turn the GPIO pin off
#        lgpio.gpio_write(h, LED, 0)
#        time.sleep(1)
#except KeyboardInterrupt:
#    lgpio.gpio_write(h, LED, 0)
#    lgpio.gpiochip_close(h)


#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17,GPIO.IN)
#GPIO.setup(27,GPIO.IN)    
#pwm = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=100)
#dir1 = gpiozero.OutputDevice(pin=4)
#dir2 = gpiozero.OutputDevice(pin=17)
#encoder = gpiozero.RotaryEncoder(a=21, b=20,max_steps=100000) 
#print("hello")
#encoder.steps = 0
#for j in range(10):
#    pwm.value = j/10
#    dir1.value = not dir1.value
#    dir2.value = not dir1.value
#    print('Duty cycle:',pwm.value,'Direction:',dir1.value)
#    time.sleep(5.0)
#    print('Counter:',encoder.steps,'Speed:',(encoder.steps)/5.0,'steps per second\n')
#    encoder.steps = 0

#pwm.value =0 
# This class has a lot more functionality,so worth reading up on it

#testing servo


from gpiozero import Servo, PWMOutputDevice
from time import sleep
servo = Servo(4,min_pulse_width=0.001, max_pulse_width=0.002,frame_width=0.0025)



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



# Testing Ultrasonic sensor
from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo = 23, trigger = 24, max_distance = 2)
while True:
    distance = ultrasonic.distance*100
    print("Distance: %.1f cm" % distance)
    # print(ultrasonic.distance)

# TRIG_PIN = 24
# ECHO_PIN = 23

# h = lgpio.gpiochip_open(0)
# lgpio.gpio_claim_output(h, TRIG_PIN)
# lgpio.gpio_claim_input(h, ECHO_PIN)

# try:
#     while True:

#         lgpio.gpio_write(h, TRIG_PIN, 0)
#         time.sleep(2)

#         lgpio.gpio_write(h, TRIG_PIN, 1)
#         time.sleep(0.00001)

#         lgpio.gpio_write(h, TRIG_PIN, 0)

#         while lgpio.gpio_read(h, ECHO_PIN) == 0:
#             pulse_send = time.time()
#             while lgpio.gpio_rad(h, ECHO_PIN) == 1:
#                 pulse_received = time.time()
#                 pulse_duration = pulse_received - pulse_send
#                 distance = round(pulse_duration*34300/2)

#                 print(f"Distance: {distance} cm")

# except KeyboardInterrupt:
#     lgpio.gpio_write(h, TRIG_PIN, 0)
#     lgpio.gpiochip_close(h)
