from socket import *
server_name = 'hostname'
server_port = 1337 

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')