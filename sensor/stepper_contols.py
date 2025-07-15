import RPi.GPIO as GPIO
import time


DIR_PIN1 = 6   
STEP_PIN1 = 24  
DIR_PIN2 = 5   
STEP_PIN2 = 23

CURRENT_MO1 = 0
CURRENT_MO2 = 0


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR_PIN1, GPIO.OUT)
    GPIO.setup(STEP_PIN1, GPIO.OUT)
    GPIO.setup(DIR_PIN2, GPIO.OUT)
    GPIO.setup(STEP_PIN2, GPIO.OUT)

def motor_rotate(step_pin, dir_pin, direction, step, step_delay):
    GPIO.output(dir_pin, direction)
    for _ in range(step):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(step_delay)


def rotate_to_position(target_position, current_position, step_pin, dir_pin):
    delta = target_position - current_position
    step_count_per_90 = 6400/4
    step = abs(delta) * step_count_per_90
    step_delay = 0.00000001
    direction = True

    if delta == 0:
        print("Don't rotate , alrady at target position")
        return current_position

    if delta > 0:
        direction = False
    else:
        direction = True
    
    motor_rotate(step_pin, dir_pin, direction, step_delay)
    return target_position



def motor_control(target_pos):
    global CURRENT_MO1, CURRENT_MO2
    if 0 <= target_pos <=3 :
        if CURRENT_MO2 != 0:
            CURRENT_MO2 = rotate_to_position(0, CURRENT_MO2, )
 
    elif 4<= target_pos < 6 :
        print("upper target")
    else:
        print("Hello world")


