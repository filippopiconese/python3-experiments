#!/usr/bin/python3

import socket

# N.B. ==> You must have root privileges in order to run the TCP_server script!
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

server_socket.bind((host, port))

server_socket.listen(3)

while True:
    client_socket, address = server_socket.accept()

    print('received connection from %s ' % str(address))

    message = 'Hello! Thank you for connecting to the server' + '\r\n '
    client_socket.send(message.encode(('ascii')))

    client_socket.close()
