import socket

def server(socket):

    HOST_CONNECTION = ''
    PORT = 5000

    # TCP
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'socket: {socket}')

    socket.bind((HOST_CONNECTION,PORT))
    listen = socket.listen()
    accept = socket.accept()

       
server(socket)