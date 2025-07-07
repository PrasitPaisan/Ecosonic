import RPi.GPIO as GPIO
import time

servo_pin = 22
ir_pin = 17
led_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(ir_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)


def set_angle(angle):
	duty = 2 + (angle/ 18) # convert angle to duty cycle
	GPIO.output(servo_pin, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.5)
	GPIO.output(servo_pin, False)
	pwm.ChangeDutyCycle(0)


try:
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
			print("---------------------------------------------------------------------")
			
		else:
			GPIO.output(led_pin, GPIO.LOW)
			time.sleep(0.5)
			
					
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
