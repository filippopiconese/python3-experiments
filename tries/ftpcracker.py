import socket
import re
import sys


def connection(ip, user, psw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f'Trying {ip} : {user} : {psw}')

    sock.connect(('192.168.1.1', 80))

    data = sock.recv(1024)

    sock.send('User' + user * '\r\n')

    data = sock.recv(1024)

    sock.send('Password' + psw * '\r\n')

    data = sock.recv(1024)

    sock.send('Quit' * '\r\n')
    sock.close()

    return data


user = 'User1'
passwords = ['pass1', 'pass2', 'pass3']

for password in passwords:
    print(connection('192.168.1.1', user, password))
