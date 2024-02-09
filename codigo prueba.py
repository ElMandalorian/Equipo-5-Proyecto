import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
MQ135 = 4
buzzer = 21
GPIO.setup(MQ135, GPIO.IN)
GPIO.setuo(buzzer, GPIO.OUT)

try:
    while True:

        if GPIO.input(MQ135):
            GPIO.output(buzzer, True)
            sleep(4)
            print("gas detectado")

        else:
            GPIO.output(buzzer, False)
            sleep(2)
            print("esperando respuesta...")
        sleep(1)

finally:
    print("limpiando...")
    GPIO.cleanup()
