import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))

template = (b"Keep-Alive=1\r\n"               # 0 или 1
            b"Content-Length=4\r\n"        # сколько байт данных
            b"Content-Type=text\r\n"          # text или file
            b"Path=/path/to/dir/or/file\r\n"  # Путь к чему-то
            b"Status=200\r\n\r\n"             # 200 успех, 404 - не найдено
            b"body")




s.sendall(template)


s.close()



