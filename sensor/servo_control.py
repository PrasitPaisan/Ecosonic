# servo_control.py
import RPi.GPIO as GPIO
import time

servo_pin = 22

pwm = GPIO.PWM(servo_pin, 50)  # 50Hz for servo
pwm.start(0)

def setup_GPIO_servo():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo_pin, GPIO.OUT)
     
def set_angle(angle):
    if 0 <= angle <= 180:
        duty = 2 + (angle / 18)  # Map angle to duty cycle
        GPIO.output(servo_pin, True)
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        GPIO.output(servo_pin, False)
        pwm.ChangeDutyCycle(0)
    else:
        raise ValueError("Angle must be between 0 and 180")

def cleanup():
    pwm.stop()
    GPIO.cleanup()
