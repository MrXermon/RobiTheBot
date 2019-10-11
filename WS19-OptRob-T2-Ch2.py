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
	# Loop until interrupted
	while True:
		Bot.forward()
		# Detect black line
		if IRSensor.AnalogRead()[3] <= 200:
			Bot.stop()
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
