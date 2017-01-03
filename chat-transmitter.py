# need two threads: receiving and outgoing.
from threading import Thread

# I think this module may be very helpful for us
# Documentation is here: https://docs.python.org/3/library/socket.html
import socket

# Initialize the socket

host = 'localhost' # localhost just means "this computer"
port = 54321       # port can be pretty much any number. This one is easy to remember.

# Create a server socket to accept incoming connections from clients.
# AF_INET means address format is IPv4
# SOCK_STREAM specifies what kind of socket it is. This one is common.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now put that socket to use on the host and port we specified above.
serverSocket.bind((host, port)) # Double parens are important to make the argument a tuple.
serverSocket.listen(0)          # This says not to keep clients queued up in line to connect... I think.


# The server socket is just here to accept incoming connections. When it does
# accept one, it creates a new client socket for the actual communication.
print("Waiting for a client to connect")
clientSocket, clientAddress = serverSocket.accept()

def ReplyPrinter(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		While True: 
			reply = sock.recv(port)
			print (reply)

thread = ReplyPrinter()
# thread is 'daemon', background task that wil quit when other threads quit.
thread.daemon()
thread.start()

# Once we have a connected receiver, begin broadcasting
print("Begin typing messages for broadcast.")
print("Type '/exit' to end the program.")
# outgoing message
message = ""
# send message to client
# Main loop that listens for messages
while message != "/exit":
	message = raw_input("message> ")
	clientSocket.send(message)
	recvmessage = peer.recv(port)
	
# Close the sockets before exiting
clientSocket.close()
serverSocket.close()
