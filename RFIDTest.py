import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Wait for you to scan a RFID card/tag")
    id = reader.read()[0]
    print("The ID for the Card/Tag is: ", id)
finally:
    GPIO.cleanup()
