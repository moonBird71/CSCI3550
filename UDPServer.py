#
#Follow the code examples from section 2.7.1 to set up the UDP sockets on UDPClient and UDPServer.

#import socket module
from socket import *

#sets variable
serverPort = 12000
#creates socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

#assigns port to the socket
serverSocket.bind(('', serverPort))

#waits for packets
print("The server is ready to receive")
while True:
    #assign variables to arriving packet data, and packet address
    message, clientAddress = serverSocket.recvfrom(2048)
    #takes input, modifies it, assigns to variable
    modifiedMessage = message.decode().upper()
    #via socket, outputs modified data to client 
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

#
#Once the sockets are set up, the communication will go as follows:

#
#The client reads a line of characters (data) from its keyboard and sends the data to the server.
#The server receives the data and converts the characters to uppercase.
#The server sends the modified data to the client.
#The client receives the modified data and displays the line on its screen.

#
#Testing: We will be executing both programs on separate consoles on your computer. Use "localhost" as the serverName on UDPClient. Run UDPServer on one console of your computer. Then run UDPClient on another console of your computer.
