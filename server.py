import socket

HOST_CONNECTION = "127.0.0.0"
PORT = 7000  

def server(socket):

    # TCP
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server started.")

    # binds socket obj to port and ip, then listens for any incoming conns
    socket.bind((HOST_CONNECTION,PORT))
    socket.listen()
    # if conn then accepts it, returns a conn and addr tuple
    conn, addr = socket.accept()
    print(f"Connection established with {addr}")

    try:
        # if up to 1024 bytes are received then adds it to data variable  then decodes it 
        # into a string
        data = conn.recv(1024)
        data_decoded = data.decode('utf-8')
        print(data_decoded)

    except OSError as e:
        print(f"Error: {e}")

    socket.close()
    

   
    

server(socket)


