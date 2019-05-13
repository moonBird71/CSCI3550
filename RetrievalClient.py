#Client that sends messages to server at loki.ist.unomaha.edu

from socket import *
serverName = 'loki.ist.unomaha.edu'
serverPort = 12000

#creates client socket using: network IPv4, and socket type TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

#initiate TCP connection to server
clientSocket.connect((serverName, serverPort))

#make a while loop to keep program going? 

#create input to send
message = raw_input('Send a message: ')

#sends message bytes into (TCP) socket
clientSocket.send(message) #need encode?

#close socket
clientSocket.close()