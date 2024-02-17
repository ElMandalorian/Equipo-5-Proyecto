import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
from time import sleep

BLYNK_AUTH_TOKEN = "BvKTL24X5prhVWsJKeOzXG5PeBytPRxw"

GPIO.setmode(GPIO.BCM)
MQ135 = 4
buzzer = 21
verde = 26
rojo = 19
GPIO.setup(MQ135, GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(verde,GPIO.OUT)
GPIO.setup(rojo,GPIO.OUT)

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

@blynk.on("V0")
def v0(value):
#    global led_switch
   if GPIO.input(MQ135):
            GPIO.output(buzzer, True)
            GPIO.output(rojo, True)
            GPIO.output(verde, False) 
            print("gas detectado")
            
   else:
            GPIO.output(buzzer,False)
            GPIO.output(verde, True)
            GPIO.output(rojo, False) 
            print("esperado respuesta...")
            
   sleep(2)
        
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 

while True:
    blynk.run()