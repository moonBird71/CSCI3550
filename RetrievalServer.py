#Server that retrieves data about client
#Works cited:
#https://docs.python.org/2/library/socket.html
#https://realpython.com/python-sockets/ 
#https://www.programcreek.com/python/example/101855/socket.html
#https://pysheeet.readthedocs.io/en/latest/notes/python-socket.html

from socket import *
serverPort = 12000

#create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#associate socket with server port number
serverSocket.bind(('', serverPort))

while True:
	#establish socket as open door/listener for a max of 1 queued connection
	serverSocket.listen(1) #server is ready
	
	print("Retrieving client data: ")
	
	#when server socket contacted, create: a socket to handshake with client socket, and client IP & port (as a tuple)
	connectionSocket, addr = serverSocket.accept() 

	##get & print client socket data:
	#get IP and port by splitting 'addr' ('ip', port')
	ip = addr[0]
	port = addr[1]
	print("\tIP address: " + ip)
	print("\tPort number: {}".format(port))
	
	buf = memoryview(bytearray(1024)) #create buffer

	#receive message from client
	##get & print message data
	numbytes = connectionSocket.recv_into(buf, 1024) #receive data (up to 'size'), store in buffer, return received in bytes
	print("\tBytes received: {}".format(numbytes))
	
	loop = raw_input("Exit? (y or n): ")
	if loop is 'y':
	    break
	
connectionSocket.close()
