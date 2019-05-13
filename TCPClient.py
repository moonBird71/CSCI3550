#Using the resources available in the textbook (particularly section 2.7.2), write a pair of programs, TCPClient and TCPServer, that use the TCP protocol to communicate with each other.

from socket import *
serverName = 'loki.ist.unomaha.edu'
serverPort = 12000

#creates client socket using: network IPv4, and socket type TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
#initiate TCP connection to server
clientSocket.connect((serverName, serverPort))
#get user input
sentence = raw_input('Input lowercase sentence: ')
#sends message bytes into (TCP) socket
clientSocket.send(sentence.encode())
#return message from server is put in variable
modifiedSentence = clientSocket.recv(1024)
#print return message
print('From Server: ' + modifiedSentence.decode())
#close socket
clientSocket.close()

#Once the sockets are set up, the communication will go as follows:

#The client reads a line of characters (data) from its keyboard and sends the data to the server.
#The server receives the data and converts the characters to uppercase.
#The server sends the modified data to the client.
#The client receives the modified data and displays the line on its screen.
#Languages: Use any language to implement this programming assignment. If using Java, here's a chapter from an older editionPreview the document (go to section 2.7). Regardless of the language used, you must name the programs, "TCPClient.<ext>" and "TCPServer.<ext>".

#Testing: We will be executing both programs on separate consoles on your computer. Use "localhost" as the serverName on TCPClient. Run TCPServer on one console of your computer. Then run TCPClient on another console of your computer.

#Submission: Upload the source code for TCPClient and TCPServer to this assignment.