import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8080))
s.listen(1)
print("Server started, waiting for connection...")

while True:
    conn, addr = s.accept()
    conn.settimeout(3)

    data = b""
    while not data.endswith(b"\r\n\r\n"):
        try:
            chunk = conn.recv(1024)

            data += chunk
        except TimeoutError as e:
            del data
            print(f"{e}, client - {addr}")
            break
    else: 
        print(len(data))
        conn.sendall(b"OK!")

    conn.close()
    print(f"This connection closed with client {addr}!")

s.close()