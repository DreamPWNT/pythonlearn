import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))


path = b"C:\\Users\\PyHS\\Desktop\\test.txt"

template = (f"Keep-Alive=1\r\n"               # 0 или 1
            f"Content-Length={len(path)}\r\n"        # сколько байт данных
            f"Content-Type=text\r\n\r\n"          # text или file

            )

template = template.encode() + path


s.sendall(template)

print(s.recv(1024*1024))
print(s.recv(1024*1024).decode())


s.close()



