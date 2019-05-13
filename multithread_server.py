#I used Python 3.7.2 64-bit on my Windows
#Web server that handles multi HTTP requests at once
#server listens for clients, send requests to another thread to handle
#thread parses request
#ip of loki server host: 137.48.187.123:12000
#ip of ec2: 172.31.26.45:12000

#citations: http://www.cs.utexas.edu/~cannata/networking/Homework/WebServer.py, https://www.geeksforgeeks.org/socket-programming-multi-threading-python/

from socket import *
from _thread import *
import sys #for terminating the program
import threading
import time
import fileinput

serverSocket = socket(AF_INET, SOCK_STREAM)
lock = threading.Lock()

#define a function for thread: will do the parsing
def processThread(connectionSocket): 
    #accepts & parses HTTP request
    message = connectionSocket.recv(1024).decode() #the received (bytes) are assigned to variable

    #error handling
    try:
        filename = message.split()[1] #splits message and assigns (item in index 1, which should be the filename) to variable
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
        lock.release()
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><h1>404 Not Found</h1></html>\r\n")
        #Close thread and socket
        lock.release()
        connectionSocket.close()

#main thread: listen for clients at a fixed port
#Prepare a server socket (bind it to an address & port)
serverSocket.bind(('', 12000)) #associate socket with port
serverSocket.listen(5) #establish socket is open for 5 (?) connections

while True:
    #Establish the connection
    print('Ready to serve...')
    
    #when socket contacts, accept and create a new socket for server to handshake with client
    connectionSocket, addr = serverSocket.accept()
    
    #start a thread to handle request
    lock.acquire()
    start_new_thread(processThread, (connectionSocket))

serverSocket.close() 