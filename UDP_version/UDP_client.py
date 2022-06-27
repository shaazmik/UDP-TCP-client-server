from socket import *

server_name = '192.168.31.201'
server_port = 1337 

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = (input('Input lowercase sentence:'))
clientSocket.sendto(message.encode(),(server_name, server_port))

returned_message, server_address = clientSocket.recvfrom(2048)
print(returned_message)

clientSocket.close()
