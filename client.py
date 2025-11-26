import socket

HOST_CONNECTION = "127.0.0.0"
PORT = 7000  

def client(socket):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST_CONNECTION, PORT))
    socket.send(b'Client: client connected and ready.')

    socket.close()
    print("Client has disconnected.")

    
    
client(socket)
   