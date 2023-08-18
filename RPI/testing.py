#  Blink an LED with the LGPIO library
#  Uses lgpio library, compatible with kernel 5.11
#  Author: William 'jawn-smith' Wilson

import time
import lgpio
import gpiozero
import multiprocessing
from multiprocessing import Value

EN_port = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=100) #RAEDM GPIO12
#ENB_port = gpiozero.OutputDevice(pin=4)

LEFT_PWM1_port = gpiozero.DigitalOutputDevice(pin=17, active_high = True,initial_value = True)
LEFT_PWM2_port = gpiozero.DigitalOutputDevice(pin=27, active_high = True,initial_value = True)

encoder = gpiozero.RotaryEncoder(a=21, b=20,max_steps=100000) 
# Step through duty cycle values, slowly increasing the speed and changing the direction of motion

encoder.steps = 0
for j in range(10):
    EN_port.value = j/10
    #ENB_port.off() #sets to 0
    
    #logic PWM1 PWM2 1 0
    PWM1_port.on()                                                                                                   
    PWM2_port.off()

    print('Duty cycle:',EN_port.value,'Direction:',PWM1_port.value, PWM2_port.value)
    time.sleep(5.0)
    print('Counter:',encoder.steps,'Speed:',(encoder.steps)/5.0,'steps per second\n')
    encoder.steps = 0

EN_port.value =0 


