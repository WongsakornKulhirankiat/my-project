import os
#import RPi.GPIO as GPIO
import Jetson.GPIO as GPIO
#from gpiozero import CPUTemperature

#CPUTemperature.Device.pin_factory=CPUTemperature.WiringPiFactory()

IR_Sensor = 31#6
Btn_OpenDoor = 11#17
Door_Status = 36#16

Btn_ShutDown = 12#18
Btn_PowerOn = 12#18

Finger_WAKE_Pin = 29#23
Finger_RST_Pin = 33#24

OP_Door = 38#20

Infrared = 22#25

#GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)#BCM
GPIO.setwarnings(False)
GPIO.setup(IR_Sensor, GPIO.IN)
GPIO.setup(Btn_ShutDown, GPIO.IN) # Switch Shutdown if low
GPIO.setup(Btn_OpenDoor, GPIO.IN) # Switch to open the door
GPIO.setup(Door_Status, GPIO.IN) # Check door open sensor

GPIO.setup(Finger_WAKE_Pin, GPIO.IN)    # wake finger
GPIO.setup(Finger_RST_Pin, GPIO.OUT, initial=GPIO.LOW)  #rest finger

GPIO.setup(OP_Door, GPIO.OUT) # Lock the door
GPIO.setup(Infrared, GPIO.OUT) # Infrared

GPIO.output(OP_Door, GPIO.LOW)

def doOpenDoor():
    GPIO.output(OP_Door, GPIO.HIGH)

def isShutdownBtn():
    return GPIO.input(Btn_ShutDown)

def isOpenDoorBtn():
    return GPIO.input(Btn_OpenDoor)

def isIRSensor():
    return GPIO.input(IR_Sensor)

# def getTemperature(): #yanaji comment out
#     return "Temperature: " + str(CPUTemperature().temperature) + "°C"

def setInfrared(VALUE):
    if VALUE not in [0,1]:
        print("invalid infrared value")
        return
    GPIO.output(Infrared, VALUE)

def setPowerOn():
    GPIO.setup(Btn_PowerOn, GPIO.IN)

def cleanup():
    GPIO.cleanup()