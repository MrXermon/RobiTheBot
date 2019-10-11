from AlphaBot2 import AlphaBot2
from TRSensor import TRSensor
import RPi.GPIO as GPIO
import time

# Initialize and set speed
Bot = AlphaBot2()
Bot.speed(40)

# Initialize IR-Sensors
IRSensor = TRSensor()

try:
	# Loop until forever
	while True:
		Bot.forward()
		# Detect black line
		if IRSensor.AnalogRead()[3] <= 200:
			# Stop and wait
			Bot.stop()
			time.sleep(1)
			
			# Drive backwards
			Bot.backward()
			time.sleep(1)
			Bot.stop()
			
			# Turn right
			Bot.right()
			time.sleep(1)
			Bot.stop()
except KeyboardInterrupt:
	GPIO.cleanup()
