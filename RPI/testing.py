#  Blink an LED with the LGPIO library
#  Uses lgpio library, compatible with kernel 5.11
#  Author: William 'jawn-smith' Wilson

import time
import lgpio
import gpiozero
import multiprocessing
from multiprocessing import Value

LEFT_EN_port = gpiozero.PWMOutputDevice(pin=21,active_high=True,initial_value=0,frequency=100) #RAEDM GPIO12
RIGHT_EN_port = gpiozero.PWMOutputDevice(pin=20,active_high=True,initial_value=0,frequency=100) #RAEDM GPIO12


LEFT_PWM1_port = gpiozero.DigitalOutputDevice(pin=19, active_high = True,initial_value = True)
LEFT_PWM2_port = gpiozero.DigitalOutputDevice(pin=26, active_high = True,initial_value = True)

RIGHT_PWM1_port = gpiozero.DigitalOutputDevice(pin=27, active_high = True,initial_value = True)
RIGHT_PWM2_port = gpiozero.DigitalOutputDevice(pin=1----------------------------------------------------------------------7, active_high = True,initial_value = True)

#encoder = gpiozero.RotaryEncoder(a=21, b=20,max_steps=100000) 
# Step through duty cycle values, slowly increasing the speed and changing the direction of motion

#encoder.steps = 0
for j in range(10):
    LEFT_EN_port.value = j/10
    RIGHT_EN_port.value = j/10
    #ENB_port.off() #sets to 0, physically connected to ground
    
    #FORWARD
    #LEFT WHEEL
    LEFT_PWM1_port.on()                                                                                                   
    LEFT_PWM2_port.off()

    #RIGHT WHEEL
    RIGHT_PWM1_port.on()                                                                                                   
    RIGHT_PWM2_port.off()

    print('Duty cycle:',LEFT_EN_port.value,'Direction:',LEFT_PWM1_port.value, LEFT_PWM2_port.value)
    time.sleep(5.0)
  #  print('Counter:',encoder.steps,'Speed:',(encoder.steps)/5.0,'steps per second\n')
 #   encoder.steps = 0


