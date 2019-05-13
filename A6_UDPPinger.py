#UDP and timeouts
#used Python 3.7.2 on Windows 64-bit
#Test using UDPPingerTest.py on Github Classroom (link on Canvas)
#Works Cited:
#https://pysheeet.readthedocs.io/en/latest/notes/python-socket.html
#https://stackoverflow.com/questions/18311338/python-udp-client-time-out-machinsm
#https://docs.python.org/2/library/socket.html 

import socket, sys, time

#set variables
serverName = 'loki.ist.unomaha.edu'
serverPort = 12000

#creates socket using: IPv4, and UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Program sends (10 in total) ping messages to server
for i in range(10):
    try:
        #rtt: need time before & after sending
        before = time.time()

        #send UDP packets (format: seq#) to server
        clientSocket.sendto(str(i + 1), (serverName, serverPort))

        #set timeout to 5 seconds
        clientSocket.settimeout(5)

        #Assuming success/packets are echoed back:
        #data, addr = socket.recvfrom(bufsize)
        data, serverAddress = clientSocket.recvfrom(2048)

        #get time (for rtt)
        rtt = (time.time()) - before

        #print: <x> bytes from <server address>: seq=<seq#> time=<rtt>
        print("{} bytes from {}: seq={} time={}".format(sys.getsizeof(data), serverAddress, data, rtt)) #print placeholder format?

    #If packet loss/timed out 
    except socket.timeout: 
        print("Request timed out.\n")

clientSocket.close()