import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from AlphaBot2 import AlphaBot2
import RPi.GPIO as GPIO
import time

# Initialize Bot and set speed
Bot = AlphaBot2()
Bot.speed(40)

# Handler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
	# Decode joystick values
	xy = self.path.split('/')
	x = float(xy[1])
	y = float(xy[2])

	# Forward and backward
	if y > 0.2:
		print("Drive forward")
		Bot.forward()
	elif y < -0.2:
		print("Drive backward")
		Bot.backward()

	# Left and right
	if x > 0.2:
		print("Turn right")
		Bot.right()
	elif x < -0.2:
		print("Turn left")
		Bot.left()

	# Stop
	if x <= 0.2 and x >= -0.2 and y <= 0.2 and y >= -0.2:
		print("Stop")
		Bot.stop()

	Bot.speed(abs(y) * 100)

#	if abs(x) > 0.9 or abs(y) > 0.9:
#		Bot.speed(100)
#	else:
#		Bot.speed(40)


        self.send_response(200)
	return


# Initialize webserver
httpd = SocketServer.TCPServer(("", 8080), MyHandler)


try:
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.server_close()
