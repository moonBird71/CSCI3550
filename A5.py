#Programming Assignment 5: Non-blocking Web Server
#Built using Visual Studio Code with Python 3.7.2 64-bit on my Windows

#Objective: work with nonblocking sockets using select() - which monitors i/o for when it becomes readable/writable (or has error)

#A4 server handles multi clients' HTTP requests, but at the cost of a new thread per socket. 
#Modern servers take an approach w/o threads: use nonblocking I/O
#Reusing A3 and A4, implement a nonblocking server that can serve HTTP requests from multi clients. 

#Works cited: https://steelkiwi.com/blog/working-tcp-sockets/,  https://pymotw.com/2/select/ 

import socket, sys, select, Queue

#create TCP socket (object)
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.setblocking(0) #set socket to non-blocking (raise exception if recv() can't receive, or send() can't send data)

#Prep a server socket (bind it to an address & port)
serverSocket.bind(('', 12000)) #associate socket with port 12000
serverSocket.listen(5) #establish socket as open for 5 connection

inputs = [serverSocket] #sockets from which we expect input
outputs = [] #sockets to which we expect to output to
message_queue = {} #queue for outgoing messages

while inputs: #loops through (and updates lists/queue)
    readable, writable, execptional = select.select(inputs, outputs, inputs) #returns 3 lists: list of sockets with readable data available, list of sockets w/ space in buffer(is writable), list of sockets w/ error
    
    for s in readable: #go through readable sockets
        if s is serverSocket: #if socket is serverSocket (the one listening for connections) then ready for new socket
            connectionSocket, addr = serverSocket.accept() #accept and create new socket to connect w/ client
            connectionSocket.setblocking(0) #set socket to non-blocking 
            inputs.append(connectionSocket) #add socket to list of inputs to monitor
            message_queue[connectionSocket] = Queue.Queue() #give socket a queue
        else: #if socket is an established client
            data = s.recv(1024) #read socket
            if data: #if data exists in socket...
                message_queue[s].put(data) #put data in queue
                if s not in outputs:
                    outputs.append(s)
            else: #if no data in socket...
                if s in outputs: #and if socket is ready to be closed...stop listening to socket
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queue[s]
    
    for s in writable: #go through writable sockets
        try:
            next_message = message_queue[s].get_nowait() #see if there is something in the queue...
        except Queue.Empty:
            outputs.remove(s) #if nothing in queue, remove from output list
        else:
            s.send(next_message) #...send next message
    
    for s in exceptional: #go through exceptional (w/error) sockets...and close them
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queue[s]