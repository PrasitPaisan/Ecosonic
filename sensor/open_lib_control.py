import RPi.GPIO as GPIO
import time
import stepper_controls as sm
import random

servo_pin = 22
led_pin = 27

class_names = ['battery', 'bottle', 'can', 'glass', 'paper', 'pingpong', 'plastic']


pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def setup_GPIO_servo():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo_pin, GPIO.OUT)
	GPIO.setup(led_pin, GPIO.OUT) 


def set_angle(angle):
	duty = 2 + (angle/ 18) # convert angle to duty cycle
	GPIO.output(servo_pin, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.5)
	GPIO.output(servo_pin, False)
	pwm.ChangeDutyCycle(0)


try:
	sm.setup_gpio()
	print("System ON")
	while True:
		
		if GPIO.input(ir_pin) == GPIO.LOW :
			GPIO.output(led_pin, GPIO.HIGH)
			print("Detected . . . ")
			time.sleep(2)
			print("Wait for AI Processing .....")
			time.sleep(4)
			print("This is a Bottle")
			print("The Door opening . . .")
			set_angle(95)
			time.sleep(3)
			set_angle(53)
			print("The door is closed")
			pred_item = random.randint(0, 6)
			time.sleep(2)
			print(f"This is a {class_names[pred_item]}")
			sm.motor_control(int(pred_item))
			print("---------------------------------------------------------------------")
			
		else:
			GPIO.output(led_pin, GPIO.LOW)
			time.sleep(0.5)
			
					
except KeyboardInterrupt:
	sm.reset_motors_position()
	pwm.stop()
	GPIO.cleanup()
