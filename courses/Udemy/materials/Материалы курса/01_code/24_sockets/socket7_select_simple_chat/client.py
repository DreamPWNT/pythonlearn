import select
import socket
import sys

if sys.platform == "win32":
    import msvcrt  # В python на Linux и Mac этого модуля нет.


END = b"\r\n"  # Конец одного сообщения.
FIN = b"\r\n\r\n"  # Клиент отключился от чата.


def read(sock: socket.socket):
    # Тут никаких изменений, и всё как обычно.
    # Тут все (любые) сообщения от всех пользователей идут через
    # один сокет от сервера (он посыльный).
    text = b""
    while True:
        data = sock.recv(1024)
        if not data:
            print("Disconnected.")  # Сервер закрылся.
            return False
        text += data
        if text.endswith(FIN):
            print(text.decode())  # Сервер закрылся. Но принтанем текст,
                                 # там может быть сообщение от пользователя ещё.
            return False
        elif text.endswith(END):
            print(text.decode().strip("\r\n"))  # Просто сообщение от пользователя.
                # Кстати, если придет сразу несколько сообщений от разных пользователей,
                # то они отпринтуются через пустую строку (раздельно), так как
                # \r\n между ними останется. 
            return True
        

def write(sock: socket.socket):
    print(">> ", end="", flush=True)
    text = sys.stdin.readline()  # input из терминала.

    sock.sendall(text.encode() + END)  # Сразу шлем на сервер в чат.
    return True


def client(sock: socket.socket):
    try:
        # Постоянный цикл чата (чтение/отправка).
        chat = True
        while chat:
            # Если Windows:
            if sys.platform == "win32":
                readable, _, _ = select.select([sock], [], [], 0.1)  # Только сокет и...
                if msvcrt.kbhit():  # ...отдельно проверяем читаемость терминала.
                    readable.append(sys.stdin)
            # Если Linux, Mac, Android, iOS, FreeBSD)))
            else:
                readable, _, _ = select.select([sock, sys.stdin], [], [])
            
            if not readable:
                continue  # Имеет смысл тут только из-за Windows кода, там есть timeout.
            
            for r in readable:  # Перебираем то что стало читаемым.
                if r is sock:  # Если сокет:
                    chat = read(sock)  # Читаем сообщение из сокета полностью.
                else:  # Если терминал:
                    chat = write(sock)  # Инпутим из терминала и отправляем в чат.
    except KeyboardInterrupt:
        # Обработка ошибки тут, потому что сигнал Ctrl+C срабатывает
        # независимо от того, делаем ли мы прям сейчас sys.stdin.readline().
        sock.sendall(FIN)


def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 8081))
    
    client(sock)
    sock.close()


if __name__ == "__main__":
    main()
    