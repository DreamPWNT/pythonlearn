import random
import select
import socket


HOST = "127.0.0.1"
PORT = 8081

END = b"\r\n"  # Конец 1 сообщения.
FIN = b"\r\n\r\n"  # Завершение чата.

CONNECTIONS = 30  # Количество активных клиентов.

BUFFERS: dict[socket.socket, bytes] = {}  # Буферы сообщений для conn клиентов.


NAMES: dict[socket.socket, bytes] = {}  # Ники для пользователей.
usernames = {  # Авто-ники для чата))) Не удержался. это делает функция
               # make_beutifull_user_name
    b"Fox", b"Owl", b"Lynx", b"Wolf", b"Hawk",
    b"Eagle", b"Falcon", b"Panther", b"Leopard", b"Tiger",
    b"Jaguar", b"Puma", b"Cat", b"Dolphin", b"Whale",
    b"Otter", b"Badger", b"Beaver", b"Ferret", b"Sable",
    b"Koala", b"Panda", b"Lemur", b"Gecko", b"Iguana",
    b"Cobra", b"Python", b"Falconet", b"Caracal", b"Serval"
}



def make_beutifull_user_name(conn: socket.socket, *, raw=False):
    """Делает красивое имя каждому пользоватлю в чате.
    Имя храниться в словаре NAMES, по ключу conn.
    Если передано raw = True, то вернет просто peername в виде:
    (ip:port), если raw = False, то будет выбрано рандомное
    название зверушки."""

    if raw:
        peer = conn.getpeername()
        NAMES[conn] = str(peer).encode()
        return

    available: set[bytes] = usernames - set(NAMES.values())
    NAMES[conn] = random.choice(list(available))
    

def sending(clients: set[socket.socket], message: bytes):
    # Рассылаем всем пользователям из clients одно сообщение.
    for client in clients:
        client.sendall(message)


def get_others(conn: socket.socket, clients: set[socket.socket]):
    return clients - {conn}  # Разница двух множеств, чтоб отобрать клиентов
                            # для рассылки.


def chat(clients: set[socket.socket]):

    # Смотим есть ли что-то от любых клиентов:
    readable, _, _ = select.select(clients, [], [], 0.1)

    # Если нет, то выходим из чата и смотрим есть ли новые connect.
    if not readable:
        return
    
    # Если есть сообщения от каких-то клиентов, то читаем;)
    for conn in readable:
        data = conn.recv(1024)
        BUFFERS[conn] += data  # Сохраняем в буфер конкретного клиента.

        # Получаем всех клиентов, кроме того от которого конкретное сообщение:
        others = get_others(conn, clients)

        # Если этот клиент просто отключился, то оповещаем всех об этом,
        # и удаляем этого клиента у нас на сервере везде:
        if not data or BUFFERS[conn].endswith(FIN):
            sending(others, f"User {NAMES[conn].decode()} disconnected. Users in chat: {len(others)}".encode() + END)
            del BUFFERS[conn]
            clients.remove(conn)
            del NAMES[conn]
            conn.close()
            continue  # CONTINUE КОТРЫЙ Я ЗАБЫЛ!!!!!!!!!

        # Если же клиент отпраавил сообщение в чат, то пересылаем его остальным,
        # при чем только если это уже полностью полученное сообщение с END в конце:
        if BUFFERS[conn].endswith(END):
            sending(others, NAMES[conn] + b": " + BUFFERS[conn])
            BUFFERS[conn] = b""
        
        # Если в чате только 1 человек, то отклбчаем его сами:
        if len(clients) == 1:
            last = clients.pop()
            last.sendall(FIN)
            last.close()
            return



def get_client(server: socket.socket, clients: set[socket.socket],
               timeout: float | None):
    """Каждый вызов этой функции - попытка подключть ОДНОГО клиента."""
    # Проверяем есть ли запрос на connect от клиентов.
    # Первых двух клиентов ждем пока они не подклбчатся по очерди.
    # Остальные запросы на connect проверяем периодически с ожиданием 0.1 сек.
    readable, _, _ = select.select([server], [], [], timeout)

    # Если запроса на connect нет, то выходим и чат продолжается.
    if not readable:
        return
    # Подключаем клиента если есть запрос на connect:
    conn, addr = server.accept()
    make_beutifull_user_name(conn)  # Рандомное имя для юзера в словаре NAME.
    print(f"Client {addr} connected!")
    # Оповещение всех в чате, что есть новый участник:
    if len(clients) > 0:
        sending(clients, f"Client {NAMES[conn].decode()} connected!".encode() + END)

    BUFFERS[conn] = b""  # Создаем буфер сообщения для conn этого клиента.
    clients.add(conn)  # Добавляем его в clients set.


def mainloop(server: socket.socket):
    """Функция с основным циклом сервера. Переключает контекст между
    чатом и подключением новых клиентов."""
    clients: set[socket.socket] = set()  # Все клиенты.

    for _ in range(2):  # Гарантированно ждем первых 2х клиентов перед началом чата.
        get_client(server, clients, None)  # Подключенные клиенты добавляются в clients.

    while len(clients) > 1:  # Чат, пока есть более 1го клиента.
        chat(clients)  # Чат. Периодически возвращаемся чтоб сделать попытку get_client.
        get_client(server, clients, 0.1)  # Подключаем новых пользователей в чат.


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(CONNECTIONS)
    print("Server started, waiting for clients...")
    mainloop(server)
    server.close()
    print("Server stopped.")


if __name__ == "__main__":
    main()
