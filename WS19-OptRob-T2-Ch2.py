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
	count = 1
	# Loop until forever
	while True:
		Bot.forward()
		# Detect black line
		if IRSensor.AnalogRead()[3] <= 800:
			print "Linie erkannt!"
			# Stop and wait
			Bot.stop()
			time.sleep(0.5)

			# Drive backwards
			Bot.backward()
			time.sleep(0.5)
			Bot.stop()

			# Turn direction
			if count % 5 == 0:
				Bot.right()
			else:
				Bot.left()

			# Wait for turn
			time.sleep(1)
			Bot.stop()

			# Increment counter
			count = count + 1

except KeyboardInterrupt:
	GPIO.cleanup()
