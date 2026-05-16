import socket
from src.decode.decode import decode_resp
def read(socket_connection: socket):
    data = socket_connection.recv(1024)
    if data == b"" :
        return None
    return data


def write(socket_connection: socket, message: str):
    socket_connection.sendall(message.encode("utf-8"))
 

def run_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 6379))
    server.listen(5)
    connected_clients_count = 0

    
    while True:
        try:
            conn, addr = server.accept() # blocking call
            print(f"Client connected: {addr}")
            connected_clients_count += 1
            while 1:
                data = read(conn)
                if not data:
                    connected_clients_count -= 1
                    print(f"Client {addr} got disconnected")
                    break
                print(f"Raw data: {data.decode('utf-8')}")
                value, _ = decode_resp(data)
                print(f"Data sent from client is : {value}, length: {len(value)}")
                
                # Respond to the client
                if value and isinstance(value, list) and value[0].upper() == "PING":
                    write(conn, "+PONG\r\n")
                else:
                    write(conn, "+OK\r\n")
                # write(conn, data.decode("utf-8"))
        except Exception as e:
            print(f"Client {addr} got disconnected: {e}")
            conn.close()
            continue

    
    
    