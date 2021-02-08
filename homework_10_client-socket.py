import socket

host = input("Enter server IP: ")
port = int(input("Enter port number: "))
obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
obj.connect((host, port))  # connect to a remote socket
msg = obj.recv(1024).decode()  # wait for a message from remote
print(msg)  # display the mesagae received from the server
message = input("Type message: ")
while message != 'q':  # breaks the connection when 'q' is sent
    obj.send(message.encode())
    data = obj.recv(1024).decode()
    print('Received from server: ' + data)
    message = input("Type message: ")
obj.close()
