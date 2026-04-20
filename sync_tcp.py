import socket


def run_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", 6379))

    server.listen(5)

    
    while True:
        conn, addr = server.accept()
        print(f"Client connected: {addr}")
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(data)

    
    
    