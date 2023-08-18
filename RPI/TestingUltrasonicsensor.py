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