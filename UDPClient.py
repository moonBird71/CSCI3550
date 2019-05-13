#Follow the code examples from section 2.7.1 to set up the UDP sockets on UDPClient and UDPServer.

#can create sockets with this
from socket import *

#sets variable to a string containing server IP or hostname (DNS)
serverName = 'loki.ist.unomaha.edu'
#set variable to an int
serverPort = 12000
#creates client socket using: IPv4 network, and UDP type socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#prompt client user for input
message = raw_input('Input lowercase sentence: ')
#via socket, send (message in bytes, to destination); [then wait]
clientSocket.sendto(message.encode(), (serverName, serverPort))
#put return packet data, and address (in the size 2040 buffer) in variables
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#prints (return packet data converted to string type)
print(modifiedMessage.decode())
#closes socket
clientSocket.close()

#
#Once the sockets are set up, the communication will go as follows:
#The client reads a line of characters (data) from its keyboard and sends the data to the server.
#The server receives the data and converts the characters to uppercase.
#The server sends the modified data to the client.
#The client receives the modified data and displays the line on its screen.

#
#Testing: We will be executing both programs on separate consoles on your computer. Use "localhost" as the serverName on UDPClient. Run UDPServer on one console of your computer. Then run UDPClient on another console of your computer.
