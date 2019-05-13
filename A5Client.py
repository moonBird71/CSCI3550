import socket, sys
serverName = 'loki.ist.unomaha.edu'
serverPort = 12000

messages = ['This is a message', 'This is another message', 'Can you hear me now?', 'Good']

clientsockets = [socket(AF_INET, SOCK_STREAM), socket(AF_INET, SOCK_STREAM)] #need to test multi client HTTP requests

for sock in clientsockets: #go through clientsockets list
    sock.connect((serverName, serverPort)) #connect to server

for m in messages: #go through messages
    for s in clientsockets: #go through sockets
        s.send(m) #send messages through sockets

    for s in clientsockets: #go through sockets
        data = s.recv(1024) #read data
        if not data: #if no data, close the socket
            s.close()