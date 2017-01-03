from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 54321
# connect to socket
sock.connect((host, port))

class ReplyPrinter(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		While True:
			reply = sock.recv(port)
			print(reply)

thread = ReplyPrinter()
thread.daemon = True
thread.start()

while True:
    message = raw_input('message>')
    sock.send(message)
