import RPi.GPIO as GPIO
import time

servo_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0) #start with 0% duty cycle

def set_angle(angle):
	duty = 2 + (angle/ 18) # convert angle to duty cycle
	GPIO.output(servo_pin, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.5)
	GPIO.output(servo_pin, False)
	pwm.ChangeDutyCycle(0)

try:
	while True:
		angle = int(input("Enter angle 0 - 180 "))
		if 0 <= angle <= 180 :
			set_angle(angle)
		else:
			print("Angle must be between 0 and 180")
			
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
