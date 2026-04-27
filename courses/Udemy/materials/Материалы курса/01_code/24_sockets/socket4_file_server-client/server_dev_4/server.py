import os
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



def list_directory(path):
    # Просто формируем через \n "список" того что есть в директории.
    try:
        items = []
        for item in os.scandir(path):
            items.append(item.path)
        return "\n".join(items).encode()
    except Exception as e:
        return str(e).encode()



def send_file(conn: socket.socket, file_path: str):
    # Вдруг файла не стало только что, на всякий случай.
    if not os.path.exists(file_path):
        send_response(conn, b"File not found", status=404)
        return

    # Нам для Content-Length нужен разме файла.
    # Размер известен, т.к. файл отправляется без изменений!!!!!
    size = os.path.getsize(file_path)

    headers = (
        f"Keep-Alive=1\r\n"
        f"Status=200\r\n"
        f"Content-Length={size}\r\n"
        f"Content-Type=file\r\n"
        f"\r\n"
    ).encode()

    # Кидаем заголовки.
    conn.sendall(headers)
    # "Туда же" следом отправляем файл, читаем его кусками.
    PAGE = 1024*4
    with open(file_path, "rb") as f:
        chunk = f.read(PAGE)
        while chunk:
            conn.sendall(chunk)
            chunk = f.read(PAGE)


def send_response(conn: socket.socket, data: bytes, status=200, data_type="text", keep_alive=1):
    # Этой функцией мы шлем любые сообщения, поэтому тут data_type="text"
    headers = (
        f"Keep-Alive={keep_alive}\r\n"
        f"Status={status}\r\n"
        f"Content-Length={len(data)}\r\n"
        f"Content-Type={data_type}\r\n"
        f"\r\n"
    ).encode()

    conn.sendall(headers)

    # Сообщение может быть разной длины, например содержимое
    # какой-то директории модет быть большим "списком".
    start, chunk_size = 0, 1024
    while start < len(data):
        conn.sendall(data[start:start + chunk_size])
        start += chunk_size


def handle_request(conn: socket.socket, headers: dict, data: bytes):
    content_type = headers.get("Content-Type", "text")

    if content_type == "file":
        file = headers.get("Path", "C:\\Users\\PyHS\\Desktop\\storage\\unknown.bin")
        with open(file, "wb") as f:
            f.write(data)
        send_response(conn, b"Uploaded to:" + file.encode(), status=200)
        return
    
    # Если клиент отправляет text, а не file, мы это видим по headers,
    # то отправим ему содержимое по информации которую он указал в body.
    path = data.decode().strip()

    if not os.path.exists(path):
        send_response(conn, b"Path not found", status=404)
        return

    # Если клиент прислал путь к директории, то отдаем ему информацию
    # о содержимом этой директории.
    if os.path.isdir(path):
        listing = list_directory(path)
        send_response(conn, listing)
        return
    
    # Если клиент прислал путь к файлу, то отдаем ему сам файл.
    if os.path.isfile(path):
        send_file(conn, path)
        return


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
        handle_request(conn, headers, data)

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