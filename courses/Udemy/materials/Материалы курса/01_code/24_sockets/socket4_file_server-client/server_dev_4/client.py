import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))

with open("C:\\Users\\PyHS\\Desktop\\test.txt", "rb") as f:
    data = f.read()



template = (f"Keep-Alive=1\r\n"               # 0 или 1
            f"Content-Length={len(data)}\r\n"        # сколько байт данных
            f"Path=C:\\Users\\PyHS\\Desktop\\storage\\uploaded.txt\r\n"
            f"Content-Type=file\r\n\r\n"          # text или file

            )

template = template.encode() + data


s.sendall(template)

print(s.recv(1024*1024))
print(s.recv(1024*1024).decode())


s.close()



