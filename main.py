import RPi.GPIO as GPIO
import dht11
import time
import datetime
import subprocess

subprocess.run(["alert", "I have awakend from my slumber!"])
# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=27)
try:
	while True:
		result = instance.read()
		print("Temperature: " + str(result.temperature) + "C")
		if result.is_valid():
			if result.temperature > 22:
				subprocess.run(["alert", "You are to hot for me! please leave..... it is like " + str(result.temperature) + "Degrees"])
			elif result.temperature < 21.6:
				subprocess.run(["alert", "You need to buy a scarf for yourself...... it is to coold"])

		time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()