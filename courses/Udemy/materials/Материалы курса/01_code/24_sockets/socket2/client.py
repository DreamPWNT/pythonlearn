import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))

text = b"H"*(1024*1024)

end = b"\r\n\r\n"

start, chunk_size = 0, 1024
while True:
    chunk = text[start: start + chunk_size]
    if chunk:
        s.sendall(chunk)
        time.sleep(1000000)
    else:
        break
    start += chunk_size

# time.sleep(100000)
s.sendall(end)

answer = s.recv(1024)
if answer == b"OK!\r\n\r\n":
    s.close()
    print("Data transfer completed!")


