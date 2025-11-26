import socket

HOST_CONNECTION = "127.0.0.0"
PORT = 7000  

def server(socket):

    # TCP
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server started.")

    socket.bind((HOST_CONNECTION,PORT))
    socket.listen()
    conn, addr = socket.accept()
    print(f"Connection established with {addr}")

    try:
        data = conn.recv(1024)
        data_decoded = data.decode('utf-8')
        print(data_decoded)

    except OSError as e:
        print(f"Error: {e}")
        
    socket.close()
    

   
    

server(socket)


