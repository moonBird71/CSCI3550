#Follow the code examples from section 2.7.2 to set up the TCP sockets on TCPClient and TCPServer.

from socket import *
serverPort = 12000
#create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#associate socket with server port number
serverSocket.bind(('', serverPort))
#establish socket as open door/listener for a max of 1 queued connection
serverSocket.listen(1)
print('The server is ready')
while True:
    #when socket is contacted, accepts it and creates a new server socket for server to complete handshake with client socket
    connectionSocket, addr = serverSocket.accept()
    #decode bytes received and assign to variable
    sentence = connectionSocket.recv(1024).decode()
    #alter message
    capitalizedSentence = sentence.upper()
    #send altered sentence as bytes through socket to client
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

#Once the sockets are set up, the communication will go as follows:

#The client reads a line of characters (data) from its keyboard and sends the data to the server.
#The server receives the data and converts the characters to uppercase.
#The server sends the modified data to the client.
#The client receives the modified data and displays the line on its screen.
#Languages: Use any language to implement this programming assignment. If using Java, here's a chapter from an older editionPreview the document (go to section 2.7). Regardless of the language used, you must name the programs, "TCPClient.<ext>" and "TCPServer.<ext>".

#Testing: We will be executing both programs on separate consoles on your computer. Use "localhost" as the serverName on TCPClient. Run TCPServer on one console of your computer. Then run TCPClient on another console of your computer.

#Submission: Upload the source code for TCPClient and TCPServer to this assignment.
