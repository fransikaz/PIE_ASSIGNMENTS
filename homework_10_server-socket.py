'''
HOMEWORK #10: Importing
PYTHON LIBRARY: Socket

-------INTRODUCTION
The socket module defines how server and client applications or processes can communicate

1. ------CREATING A SOCKET----------------

The first thing to do is to import the socket module using any of the options below

import socket / from socket import *

then create an object which will define the parameters for the connection

>>> object = socket.socket(family,type,protocol)

the object name can be set to anything string. In this example will use server for the server side
and client for the client side

-family: designates the address family to be used by the socket and is set to AF_INET by default
but has other acceptable values such as AF_INET6.
     AF_INET is IP address version 4 (IPv4)
     AF_NET6 is IPv6
-type: is type of connection and by default is set to SOCK_STREAM for connection-oriented (TCP).
     or SOCK_DGRAM for connectionless (UDP)
-protocol: is usually set to o

2. ------SOCKET METHODS-----------

There are two types of socket methods namely, server socket methods and client socket methods
server side methods include bind(), listen(), accept(), send().

syntax
>>> socket.bind((host,port))
     binds the socket to an IP address and port number
     host can be set to 'localhost' or use socket.gethostname() in place of 'localhost'
     port is the com port number
>>> socket.listen(3)
     tells the server to actively listen to connection requests from clients
     the number 3 is a bcaklog and denotes the number of connection attempts before before refusing
>>> socket.accept()
     accepts the requests received when server parameters are matched by request
     identifies the client using client IP address and port number
>>> socket.send()
     server sends data to client using the client IP address and port number
>>> socket.recv()
     receives data from client
>>> socket.close()
     closes the connection

client side methods include connect(),send(),recv()

>>>socket.connect((host,port))
    the connect method takes in two arguments, the server IP address and port number
    it initiates the connection with the server by sending a request
    once the request is accepted by the server, the connection is established
    and data transmission can ensue
>>> socket.send()
     client sends data to the server using the ip address and port number specified in the connect method
     buffer sizze can
>>> socket.recv()
     client receives data from server
     buffer size can be set as an argument
>>> socket.close()
     closes the connection and data transmission is stopped

'''
# LETS NOW SET THE SERVER SIDE PROGRAM
# Client side will be set on a different python file
# then run the two files in separate command windows
import socket

# host = '127.0.0.1'
# port = 7777
# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to IP address and pport number
server.bind(('localhost', 9999))
# tells server to listen to connection requests
server.listen()
# accepts connection and IDs the client with IP address and port number
conn, addr = server.accept()
welcome = "Connection established!"
# sends connection established message to client
conn.send(welcome.encode())
# displays connection status
print("Connection established with " + str(addr))
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    # print("from connected  user: " + str(data))
    data = str(data).upper()
    print("Received from User: " + str(data))
    data = input("Type message: ")
    conn.send(data.encode())
conn.close()
