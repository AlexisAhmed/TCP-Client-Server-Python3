#!/usr/bin/pyhton3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substitued with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection 
    clientsocket, address = serversocket.accept()

    print("received connection from " % str(address))

    message = 'hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message)

    clientsocket.close()
