import socket

# Как выглядит НАШ протокол, просто пример,
# эта переменная нигде не используется:
template = (b"Keep-Alive=1\r\n"               # 0 или 1
            b"Content-Length=2659\r\n"        # сколько байт данных
            b"Content-Type=text\r\n"          # text или file
            b"Path=/path/to/dir/or/file\r\n"  # Путь к чему-то
            b"Status=200\r\n\r\n"             # 200 успех, 404 - не найдено
            b"body")                          # тело запроса
# одиночный \r\n - разделитель между разыными значениями заголовков;
# двойной \r\n\r\n - разделитель заголовков, от самого тела запроса (то что передается)


IPv = socket.AF_INET
SOCK_TYPE = socket.SOCK_STREAM

HOST = "127.0.0.1"
PORT = 8080

CONNECTIONS = 1
CLIENT_TIMEOUT = 3



def get_request(conn: socket.socket):
    buffer = b""

    # Читаем заголовки тоже циклично из общего "потока" байт
    while b"\r\n\r\n" not in buffer:  # пока не встретим \r\n\r\n
        chunk = conn.recv(1024)
        if not chunk:
            return {}, b"", False
        buffer += chunk

    # Берем байты заголовков в headers, а часть самого запроса в body.
    headers_raw, body = buffer.split(b"\r\n\r\n", 1)

    # Делаем из байт заголовка словарь.
    headers = {}
    for line in headers_raw.split(b"\r\n"):
        key, value = line.split(b"=", 1)
        headers[key.decode()] = value.decode()

    content_length = int(headers.get("Content-Length", "0"))
    keep_alive = int(headers.get("Keep-Alive", "0"))

    # Переменная body у нас уже есть, дочитываем туда всё остальное
    # "тело" запроса. Читаем четко по Content-Length.
    while len(body) < content_length:
        chunk = conn.recv(1024)
        if not chunk:
            return {}, b"", False
        body += chunk

    body = body[:content_length]

    return headers, body, keep_alive
    


def handle_connection(conn: socket.socket, addr: tuple):
    try:
        headers, data, keep_alive = get_request(conn)
        if not data:
            raise ConnectionError("The client suddenly shut down.")
        print(headers)
        print(data)
        print(keep_alive)

    except socket.timeout as e:
        print(f"{e}, client - {addr}")
    except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError) as e:
        print("Connection was reset...")
    except ConnectionError as e:
        print(e)
    finally:
        conn.close()
        print(f"This connection closed with client {addr}!")


def get_connections(sock: socket.socket):
    while True:
        conn, addr = sock.accept()
        conn.settimeout(CLIENT_TIMEOUT)
        handle_connection(conn, addr)


def main():
    with socket.socket(IPv, SOCK_TYPE) as sock:
        sock.bind((HOST, PORT))
        sock.listen(CONNECTIONS)
        print("Server started, waiting for connection...")
        get_connections(sock)


if __name__ == "__main__":
    main()