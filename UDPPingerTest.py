# UDPPingerTest.py
# modified from Kurose to produced a predictable packet lost pattern for testing purposes
from socket import *
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
pktlosspattern = [1,0,0,1] # 1 means keep the packet
pattndx = 0
while True:
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	# Capitalize the message from the client
	message = message.upper()
	# if the current pattern is a 1, send it back
	if pktlosspattern[pattndx]:
		serverSocket.sendto(message, address)
	pattndx = (pattndx + 1) % len(pktlosspattern) 