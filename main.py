import gpiozero
import time

# https://www.raspberrypi.org/documentation/usage/gpio/
# "Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19"

# Setup PWM and direction GPIO.
pwm1 = gpiozero.PWMOutputDevice(pin=12, active_high=True, initial_value=0, frequency=50000)
direction1 = gpiozero.OutputDevice(pin=4)

# Setup rotary encoder.
encoder = gpiozero.RotaryEncoder(a=2, b=3, max_steps=100000)

# Set PWM value with:
# A number
# pwm1.value = 10

# Set direction value with:
# Either true or false
# direction.value = true

# Directions
FORWARDS = True
BACKWARDS = False

# Motors
LEFT = "left"
RIGHT = "right"


def configure_movement():
    None

def set_motor(name, speed, direction):
    None


# Configure second motor... Duplicate of above.
# pwm2 = gpiozero.PWMOutputDevice(pin=12, active_high=True, initial_value=0, frequency=50000)
# direction2 = gpiozero.OutputDevice(pin=4)

# pre_steps = 0
# for j in range(10):
#     pwm.value = j / 10
#     direction.value = not direction.value
#     print("Duty cycle:", pwm.value, "Direction:", direction.value)
#     time.sleep(5.0)
#     print("Counter:", encoder.steps, "Speed:", (encoder.steps - pre_steps) / 5.0, "steps per second\n")
#     pre_steps = encoder.steps


#defining sensors
frontSensor = DistanceSensor(echo=38, trigger=13, max_distance=1, threshold_distance=0.1)
backSensor = DistanceSensor(echo=40, trigger=15, max_distance=1)
leftSensor = DistanceSensor(echo=32, trigger=7, max_distance=1)
rightSensor = DistanceSensor(echo=36, trigger=11, max_distance=1, threshold_distance=0.1)


def senseFront():
    frontSensor.when_in_range = senseSides()

def senseBack():
    backSensor.when_in_range = senseSides()

def senseSides():
    #stop motion
    if leftSensor.distance<0.1
        #turn right
    elif rightSensor.distance<0.1
        #turn left
    else
        #turn right
