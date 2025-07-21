from RPi.GPIO import GPIO

IR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

def read_ir_sensor():
    return GPIO.input(IR_PIN)
