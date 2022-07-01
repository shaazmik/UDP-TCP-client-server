from socket import *
from sqlite3 import connect
import sys 
import logging



Max_port_value = 65535



def TCP_client(server_name, server_port):
    
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    message = input("Input lowercase message: ")
    client_socket.send(message)

    modified_message = client_socket.recv(2048)

    print("From server: ", modified_message)

    client_socket.close

    return 



def TCP_server(server_name, server_port):

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(server_name, server_port)
    server_socket.listen(1)

    print("The server is ready to receive")

    while 1:
        connection_socket, client_address = server_socket.accept()
        
        message          = connection_socket.recv(2048)
        modified_message = message.upper()
        connection_socket.send(modified_message)
        
        connection_socket.close() 



def check_arguments(argv):
    
    if argv[2].isdigit():

        if (int(argv[2]) < 0 or int(argv[2]) > Max_port_value):
            return 0

        if (argv[1].count('.') == 3):
            ip_digits = argv[1].split('.')

            if (ip_digits[0].isdigit() and ip_digits[1].isdigit() and ip_digits[2].isdigit() and ip_digits[3].isdigit()):

                ip_digits = [int(value) for value in ip_digits]

                for i in ip_digits:
                    if (i < 0) or (i > 255):
                        return 0

                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0



def prepare_logging():
    
    logger  = logging.getLogger('__name__')
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(stream = sys.stdout)
    logger.addHandler(handler)
    handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))

    return logger



if __name__ == '__main__':
    #server_name2 = '127.0.0.1' (for check yourself)
    #server_port = 1337 (more than 1024)

    logger = prepare_logging()


    if len(sys.argv) < 4:
        logger.error("Wrong number of arguments")

    else:
        if (check_arguments(sys.argv) != 0):
            if (sys.argv[3] == '-s'):

            elif (sys.argv[3] == '-c'):
                
            else:
                logger.error("Wrong type of flag\n")
                logger.info("\nType of input:\n"
                            "py <namefile>.py <ip> <port> <flag>\n"
                            "-s flag starts the program as server side\n"
                            "-c flag starts the program as server side\n")
            
        else:
            logger.error("Wrong type of IP or port\n")
            logger.info("\nType of input:\n"
                           "py <namefile>.py <ip> <port> <flag>\n"
                           "-s flag starts the program as server side\n"
                           "-c flag starts the program as server side\n")
