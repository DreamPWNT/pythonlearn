import os
import socket
import shlex


HOST = "127.0.0.1"
PORT = 8080

END_HEADERS = b"\r\n\r\n"
CHUNK = 4096
TIMEOUT = 5

KEEP_ALIVE = True

# Значения статусов по нашему протоколу.
STATUSES = {
    "200": "OK",
    "400": "Bad Request",
    "404": "Not Found"
}


#################  Отправка и чтение запросов ###############################
def send_file(sock: socket.socket, *, file_path: str, remote_path: str) -> None:
    """Отправляем файл без каких либо сложностей.
    Просто следуем протоколу и формируем правильные заголовки.

    Args:
        conn (socket.socket): Очевидно.
        file_path (str): Путь к файлу на устройстве клиента.
        remote_path (str): Путь к файлу на сервере (куда и под каким именем сохранять).
    """
    size = os.path.getsize(file_path)

    headers = (
        f"Keep-Alive=1\r\n"
        f"Content-Length={size}\r\n"
        f"Path={remote_path}\r\n"
        f"Content-Type=file\r\n"
        f"\r\n"
    ).encode()
    # Кидаем заголовки.
    sock.sendall(headers)
    # "Туда же" следом отправляем файл.
    with open(file_path, "rb") as f:
        sock.sendfile(f)


def send_request(sock: socket.socket, *, path: str, content_type="text", keep_alive=1) -> None:
    """Шлем запрос на сервер по типу get. Только заголовки, тела нет.

    Args:
        sock (socket.socket): Очевидно.
        path (str): Путь к директории или файлу на сервере.
        content_type (str, optional): Defaults to "text".
        keep_alive (int, optional): Defaults to 1.
    """
    headers = (
        f"Keep-Alive={keep_alive}\r\n"
        f"Content-Type={content_type}\r\n"
        f"Path={path}\r\n"  # Или путь к директории или к файлу на сервере.
        f"\r\n"
    ).encode()

    sock.sendall(headers)


def _recv_exact(sock: socket.socket, *, n: int) -> bytes:
    """Вспомогательная функция, чтоб вынести часть кода отдельно.
    Прочитать ровно n байт или выбросить ошибку при EOF.
    Просто отдельно в функции дочитываем тело."""
    rest_of_body = b""
    while len(rest_of_body) < n:
        chunk = sock.recv(min(CHUNK, n - len(rest_of_body)))  # Защита от лишних байт.
        if not chunk:
            raise ConnectionError("Connection closed while reading body")
        rest_of_body += chunk
    return rest_of_body


def receive_response(sock: socket.socket) -> tuple[dict, bytes]:
    """Тут "как обычно", чтение как и у сервера происходит.

    Args:
        sock (socket.socket): .

    Raises:
        ConnectionError: Если сервер неожиданно закрылся.

    Returns:
        tuple[dict, bytes]: Заголовки и тело.
    """
    buffer = b""

    # читаем заголовки
    while END_HEADERS not in buffer:
        chunk = sock.recv(CHUNK)
        if not chunk:
            # Да, тут конечно тоже можно поднять ошибку, вы можете
            # проектирвоать как это будет удобно в анном случае.
            raise ConnectionError("Connection closed while reading headers")
        buffer += chunk

    headers_raw, body = buffer.split(END_HEADERS, 1)

    # Парсим заголовки точно так же как и на сервере всё в основном.
    headers = {}
    for line in headers_raw.split(b"\r\n"):
        key, value = line.split(b"=", 1)
        headers[key.decode()] = value.decode()

    content_length = int(headers.get("Content-Length", "0"))

    # Дочитываем тело когда оно есть.
    if len(body) >= content_length:
        body = body[:content_length]  # Защита от лишних байт.
    else:
        body = body + _recv_exact(sock, n=content_length - len(body))

    return headers, body


######################  Сценарии запросов ###################################
def request_path(sock: socket.socket, *, path: str) -> bool:
    """Обработка ls <path> команды.
    Шлем запрос на сервер для получения содержимого директории и...
    - получаем ответ. Если статус ответа не 200, пишем о ошибке, иначе
    выводим в терминал ответ от сервера. Сервер присылает байты ответа (текста)
    в body.

    Args:
        sock (socket.socket): .
        path (str): Путь к директории на сервере.

    Returns:
        bool : Keep-Alive or not Keep-Alive.
    """
    # Шлем запрос в заголовке Path будет path для просмотра содержимого.
    send_request(sock, path=path)
    # В data строка со списком содержимого path на сервере.
    headers, data = receive_response(sock)

    status = headers.get("Status")
    keep_alive = bool(int(headers.get("Keep-Alive", "0")))
    # Если ответ с статусом об ошибке, то выходим из функции.
    # Принтуем ошибку на основании статуса. body в таком случае нет.
    if status != "200":
        print("Error:", STATUSES[status])
        return keep_alive

    # Работает если сервер прислал "список" содержимого директории.
    print(data.decode(errors="ignore"))
    # Возвращаем значение заголовка будет ли дальше общение.
    return keep_alive


def download_file(sock: socket.socket, *, remote_path: str, local_path: str) -> bool:
    """Обраблотка dd <remote> <local> команды.
    Скачиваем файл с сервера. Без сложностей, отдеьлных загрузок
    в временные файлы делать не будем (чтоб не тратить время и
    не усложнять уже очевидное).

    Args:
        sock (socket.socket): .
        remote_path (str): Путь к файлу на сервере, который скачивать.
        local_path (str): Куда и под каким именем загружать.

    Returns:
        bool : Keep-Alive or not Keep-Alive.
    """
    # Отправляем запрос "дай мне файл".
    send_request(sock, path=remote_path)
    # Читаем ответ. В data принятые байты файла (по простому).
    headers, data = receive_response(sock)
    # Если ответ с статусом об ошибке, то выходим из функции.
    keep_alive = bool(int(headers.get("Keep-Alive", "0")))
    status = headers.get("Status")

    if status != "200":
        print("Error:", STATUSES[status])
        return keep_alive

    with open(local_path, "wb") as f:
        f.write(data)

    print(f"File saved as: {local_path}")
    # Возвращаем значение заголовка будет ли дальше.
    return keep_alive



def upload_file(sock: socket.socket, *, local_path: str, remote_path: str) -> bool:
    """Обработка команды ud <local> <remote>.

    Args:
        sock (socket.socket): .
        local_path (str): Путь к файлу который будет загружаться на сервер.
        remote_path (str): Куда грузить на сервер и как называется.

    Returns:
        bool : Keep-Alive or not Keep-Alive.
    """

    if not os.path.isfile(local_path):
        print("File not found:", local_path)
        return KEEP_ALIVE
    # Шлем файл на сервер и заголовки там же будут делаться:
    send_file(sock, file_path=local_path, remote_path=remote_path)
    # В ответе в body текстовое сообщение от сервера, пока так.
    headers, _ = receive_response(sock)  # body нет, заменил на _

    print(STATUSES[headers.get("Status")])
    # Возвращаем значение заголовка будет ли дальше.
    return bool(int(headers.get("Keep-Alive", "0")))



#################  CLI и Установка соединения ###############################
def print_help() -> None:
    print('\033[1;32m', end='')  # Не удержался... Сила воли так себе xD
    print('Commands:')
    print('  ls <path>                    - list directory')
    print('  dd <remote> <local>          - download file')
    print('  ud <local> <remote>          - upload file')
    print('  help                         - show this help')
    print('  exit                         - quit')
    print('')
    print('Paths with spaces use quotes:')
    print('  dd "/remote dir/file.txt" "/local path/file.txt"')
    print('---------------------------------------------------')
    print('\033[0m', end='')


def cli(sock: socket.socket) -> bool:
    """В зависимости от input клиента (пользователя) запускает
    соответствующие функции по взаимодействию с сервером.

    Args:
        sock (socket.socket): Будет пробрасываться выше по стеку.

    Raises:
        KeyboardInterrupt: Для команды exit. Тут это показалось удобным,\
            так как есть except в main.

    Returns:
        bool : Keep-Alive or not Keep-Alive.
    """
    line = input("> ").strip()
    if not line:
        print("Was empty input.")
        return KEEP_ALIVE

    try:
        # Тут мы проверяем на правильность ввода вариантов команд.
        parts = shlex.split(line, posix=False)
        if parts[0] not in ["ls", "dd", "ud", "exit", "help"]:
            raise ValueError("Wrong command!")
        elif len(parts) > 3:
            raise ValueError("Too many args!")
        elif parts[0] == "ls" and len(parts) != 2:
            raise ValueError("Use ls <path>!")
        elif parts[0] in ["exit", "help"] and len(parts) > 1:
            raise ValueError("If u even can't ask for help or exit,\
                             maybe don't touch anything! ;D Joke! Just be more careful!)))")
    # Тут же обрабатываем и после сообщения выходим из cli().
    except ValueError as e:
        print("\033[1;31m", end="")
        print("Parse error:", e)
        print("Type 'help'.")
        print("\033[0m", end="")
        return KEEP_ALIVE
    # Если всё ОК с вводом команды, то уже решаем что делать дальше.
    cmd = parts[0]

    if cmd == "exit":
        # Убрал тут raise KeyboardInterrupt так как уже рассказал про этот момент.
        print("\nBye!")
        return not KEEP_ALIVE

    elif cmd == "help":
        print_help()
        return KEEP_ALIVE

    elif cmd == "ls":
        keep_alive = request_path(sock, path=parts[1].strip('"'))
        return keep_alive

    elif cmd == "dd":
        keep_alive = download_file(sock, remote_path=parts[1].strip('"'), local_path=parts[2].strip('"'))
        return keep_alive

    elif cmd == "ud":
        keep_alive = upload_file(sock, local_path=parts[1].strip('"'), remote_path=parts[2].strip('"'))
        return keep_alive
    else:
        print("Unknown command.")  # На последок или напоследок, чтоб наверняка.
        return KEEP_ALIVE


def main() -> bool:
    try:
        # keep_alive используется для двух целей:
        #    - продолжать ли общение на том же подключении (основная задача);
        #    - возвращается из функции main при завершении соединения как маркер,
        #      нужно ли переподключаться к серверу.
        keep_alive = KEEP_ALIVE

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            sock.connect((HOST, PORT))

            print("Connected to server.")

            while keep_alive:
                try:
                    keep_alive = cli(sock)
                except socket.timeout:
                    print("\033[1;31m", end="")
                    print("Timeout: server did not respond in time.")
                    print("\033[0m", end="")
                    keep_alive = True  # Оставляем True как маркер для переподключения, но
                    break   # рвем текущее подключение.
                except KeyboardInterrupt:
                    print("\nBye!")
                    keep_alive = False

    except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
        print("\033[1;31m", end="")
        print("Connection was reset.")
        print("\033[0m", end="")
    except ConnectionRefusedError as e:  # Сервер не работает, не удалось connect.
        print("\033[1;31m", end="")
        print(e)
        print("\033[0m", end="")
        keep_alive = False  # Переподключаться не нужно.
    except ConnectionError as e:
        print("\033[1;31m", end="")
        print("Connection error:", e)
        print("\033[0m", end="")
    
    # Возвращаем keep_alive УЖЕ КАК маркер нужно ли пытаться переподключаться к серверу.
    return keep_alive



if __name__ == "__main__":
    print_help()
    reconnect = True
    while reconnect:  # Цикл переподключения к серверу.
        reconnect = main()
