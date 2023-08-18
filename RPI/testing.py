#  Blink an LED with the LGPIO library
#  Uses lgpio library, compatible with kernel 5.11
#  Author: William 'jawn-smith' Wilson

import time
import lgpio
import gpiozero

pwm = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=100) #RAEDM GPIO12
dir1 = gpiozero.OutputDevice(pin=4)
dir2 = gpiozero.OutputDevice(pin=17)
encoder = gpiozero.RotaryEncoder(a=21, b=20,max_steps=100000) 
# Step through duty cycle values, slowly increasing the speed and changing the direction of motion
dir1.on() #sets to 3.3v
encoder.steps = 0
for j in range(10):
    pwm.value = j/10
    
    dir2.off()
    print('Duty cycle:',pwm.value,'Direction:',dir1.value)
    time.sleep(5.0)
    print('Counter:',encoder.steps,'Speed:',(encoder.steps)/5.0,'steps per second\n')
    encoder.steps = 0

pwm.value =0 

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