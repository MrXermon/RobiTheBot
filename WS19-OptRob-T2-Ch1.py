from AlphaBot2 import AlphaBot2
import RPi.GPIO as GPIO
import time

# Initialize Bot and set speed
Bot = AlphaBot2()
Bot.speed(40)

try:
	# Loop until forever
	while True:
		# Drive forwards
		Bot.forward()
		time.sleep(1)

		# Stop an wait
		Bot.stop()
		time.sleep(1)

		# Drive backwards
		Bot.backward()
		time.sleep(1)

		# Stop and wait
		Bot.stop()
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
