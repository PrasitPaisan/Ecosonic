# motor_control.py
import RPi.GPIO as GPIO
import time

# GPIO Pins
MOTOR1_STEP = 18    
MOTOR1_DIR = 23
MOTOR2_STEP = 24
MOTOR2_DIR = 25

# Constants
STEP_ANGLE = 1.8
STEPS_PER_90_DEG = int(90 / STEP_ANGLE)
STEP_DELAY = 0.001

# Defind initail positions for motors
motor1_position = 1
motor2_position = 1

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR1_STEP, GPIO.OUT)
    GPIO.setup(MOTOR1_DIR, GPIO.OUT)
    GPIO.setup(MOTOR2_STEP, GPIO.OUT)
    GPIO.setup(MOTOR2_DIR, GPIO.OUT)

def rotate_motor(step_pin, dir_pin, direction, steps):
    GPIO.output(dir_pin, direction)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(STEP_DELAY)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(STEP_DELAY)

def rotate_to_position(current_pos, target_pos, step_pin, dir_pin):
    delta = target_pos - current_pos
    steps_needed = abs(delta) * STEPS_PER_90_DEG

    if delta == 0:
        print("Don't rotate, already at target position.")
        return current_pos

    direction = GPIO.HIGH if delta > 0 else GPIO.LOW
    rotate_motor(step_pin, dir_pin, direction, steps_needed)
    return target_pos

def control_motors_by_input(value):
    global motor1_position, motor2_position

    if 1 <= value <= 4:
        if motor2_position != 0:
            motor2_position = rotate_to_position(
                motor2_position,
                0, 
                MOTOR2_STEP,
                MOTOR2_DIR
            )
        motor1_position = rotate_to_position(
            motor1_position,
            value,
            MOTOR1_STEP,
            MOTOR1_DIR
        )
    elif 5 <= value <= 8:
        motor2_position = rotate_to_position(
            motor2_position,
            value - 4,
            MOTOR2_STEP,
            MOTOR2_DIR
        )
    else:
        print("The value must be between 1 and 8.")

def cleanup():
    GPIO.cleanup()

