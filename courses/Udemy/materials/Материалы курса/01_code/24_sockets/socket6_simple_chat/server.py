import socket


HOST = "127.0.0.1"
PORT = 8081

END = b"\r\n"  # Конец 1 сообщения.
FIN = b"\r\n\r\n"  # Завершение чата.

CONNECTIONS = 2  # ТОЛЬКО 2 клиента в этом варианте кода.


def relay(sender: socket.socket,
          receiver: socket.socket) -> bool:
    """
    Принимает сообщение от sender и
    пересылает receiver.
    Возвращает False если диалог закончен.
    """
    buffer = b""

    while True:
        data = sender.recv(1024)

        # клиент закрыл соединение
        if not data:
            receiver.sendall(b"user disconnected" + FIN)
            return False

        buffer += data

        # пользователь завершил работу
        if buffer.endswith(FIN):
            receiver.sendall(b"user disconnected" + FIN)
            return False

        # обычное сообщение
        if buffer.endswith(END):
            receiver.sendall(buffer)
            return True


def chat(clients: list[socket.socket]):
    # В списке clients 2 сокета клиентов.
    # Главный цикл сервера
    while True:
        # сообщение от клиента 1 - клиенту 2
        if not relay(clients[0], clients[1]):
            break
        # Меняем conn клиентов в списке местами:
        # clients.reverse()  # Или так.
        clients[0], clients[1] = clients[1], clients[0]  # Или так.


def get_clients(server: socket.socket):
    clients: list[socket.socket] = []
    # принимаем ДВА клиента
    for _ in range(CONNECTIONS):
        conn, addr = server.accept()
        print(f"Client {addr} connected!")
        clients.append(conn)
    else:
        clients[0].sendall("Your friend connected!".encode() + END)

    print(f"{CONNECTIONS} clients connected. Chat started.")

    chat(clients)
    for client in clients:
        client.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(CONNECTIONS)  # два клиента одновременно
    print("Server started, waiting for 2 clients...")
    get_clients(server)
    server.close()
    print("Server stopped.")


if __name__ == "__main__":
    main()