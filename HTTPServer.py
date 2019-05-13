#Web server that handles 1 HTTP request at a time
#server accepts and parses HTTP request; get requested file from own file system, create an HTTP response message with header lines and requested file, then send response to client
#if file not in server, sends HTTP "404 Not Found" message to client
#need ip of server host: 137.48.187.123:12000
#See the description of Socket Programming Assignment 1 at the end of Chapter 2.

#citations: http://www.cs.utexas.edu/~cannata/networking/Homework/WebServer.py

#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket (bind it to an address & port??)
serverSocket.bind(('', 12000)) #associate socket with port??
serverSocket.listen(1) #establish socket as open for 1 connection

while True:
    #Establish the connection
    print('Ready to serve...')
    
    #when socket contacts, accept and create a new socket for server to handshake with client
    connectionSocket, addr = serverSocket.accept()
    try:
        #accepts & parses HTTP request
        message = connectionSocket.recv(1024).decode() #the received (bytes) are assigned to variable
        filename = message.split()[1] #splits message and assigns (item in index 1) to variable
        
        #get requested file
        f = open(filename[1:]) #open (char 1 onward) and assign
        #create HTTP response with header lines and file
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n") #??check header convention
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n") #??check if convention
        #Close client socket
        connectionSocket.close()

serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data 
