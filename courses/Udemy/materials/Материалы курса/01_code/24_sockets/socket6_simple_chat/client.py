import socket


END = b"\r\n"  # Конец 1 сообщения.
FIN = b"\r\n\r\n"  # Завершение чата.



def read(sock: socket.socket):
    text = b""
    while True:
        data = sock.recv(1024)
        if not data:
            print("Disconnected.")
            return False
        text += data
        if text.endswith(FIN):
            print(text.decode())
            return False
        elif text.endswith(END):
            print(text.decode())
            return True
        

def write(sock: socket.socket):
    try:
        text = input(">> ")
    except KeyboardInterrupt:
        sock.sendall(FIN)
        return False
    sock.sendall(text.encode() + END)
    return True


def client(sock: socket.socket):
    # chat = True
    # while chat:
    #     chat = read(server)
    #     if chat:
    #         chat = write(server)
    while read(sock) and write(sock):
        pass  # всякие полезные действия.



def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 8081))
    
    client(sock)
    sock.close()


if __name__ == "__main__":
    main()