import socket

HOST_CONNECTION = "127.0.0.0"
PORT = 7000  

def server(socket):

    # TCP
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("server started")

    
    
    socket.bind((HOST_CONNECTION,PORT))
    socket.listen()
    conn, addr = socket.accept()

    try:
        data = socket.recv(1024)
        data.decode("ascii")

    except OSError as e:
        print(f"Error: {e}")

    # print(f"{conn}, {addr} connected to the server!")
    socket.close()
    

   
    

server(socket)


