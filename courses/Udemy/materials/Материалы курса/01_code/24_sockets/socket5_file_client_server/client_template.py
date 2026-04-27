import socket
import shlex


HOST = "127.0.0.1"
PORT = 8080

END_HEADERS = b"\r\n\r\n"
CHUNK = 4096
TIMEOUT = 5

KEEP_ALIVE = True

#################  Отправка и чтение запросов ###############################
def send_file(conn: socket.socket, *, file_path: str, remote_path: str):
    pass

def send_request(sock: socket.socket, *, path: str, content_type="text", keep_alive=1):
    pass

def receive_response(sock: socket.socket):
    pass

######################  Сценарии запросов ###################################
def request_path(sock: socket.socket, *, path: str):
    pass

def download_file(sock: socket.socket, *, remote_path: str, local_path: str):
    pass

def upload_file(sock: socket.socket, *, local_path: str, remote_path: str):
    pass

#################  CLI и Установка соединения ###############################
def print_help():
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


def cli(sock: socket.socket):
    """_summary_

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
        parts = shlex.split(line)
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
    cmd = parts[0].lower()

    if cmd == "exit":
        # Иногда нормально, но нужно помнить, что может "затеряться" в коде и потом,
        # будет неясно почему это возникает (не очевидно).
        raise KeyboardInterrupt()

    elif cmd == "help":
        print_help()
        return KEEP_ALIVE

    elif cmd == "ls":
        keep_alive = request_path(sock, path=parts[1])
        return keep_alive

    elif cmd == "dd":
        keep_alive = download_file(sock, remote_path=parts[1], local_path=parts[2])
        return keep_alive

    elif cmd == "ud":
        keep_alive = upload_file(sock, local_path=parts[1], remote_path=parts[2])
        return keep_alive
    else:
        print("Unknown command.")  # На последок или напоследок, чтоб наверняка.
        return KEEP_ALIVE


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            sock.connect((HOST, PORT))

            print("Connected to server.")

            keep_alive = KEEP_ALIVE
            while keep_alive:
                try:
                    keep_alive = cli(sock)
                except socket.timeout:
                    print("\033[1;31m", end="")
                    print("Timeout: server did not respond in time.")
                    print("\033[0m", end="")
                except KeyboardInterrupt:
                    print("\nBye!")
                    keep_alive = False
                    break

    except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
        print("\033[1;31m", end="")
        print("Connection was reset.")
        print("\033[0m", end="")
    except ConnectionError as e:
        print("\033[1;31m", end="")
        print("Connection error:", e)
        print("\033[0m", end="")



if __name__ == "__main__":
    print_help()
    main()
