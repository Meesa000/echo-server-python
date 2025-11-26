import socket

HOST_CONNECTION = "127.0.0.0"
PORT = 7000  

def client(socket):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST_CONNECTION, PORT))
    socket.send(b'Client ready')
    socket.close()

    
    
client(socket)
   