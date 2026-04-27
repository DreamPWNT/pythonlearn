import socket
import time


HOST = "127.0.0.1"
PORT = 8081

# SOCK_DGRAM - сокет с протоколом UDP.
server = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print("Server started.")

while True:
    data, addr = server.recvfrom(1200)  # 1 пакет за раз.
    print(data, addr)
    server.sendto(b"Answer!", addr)  # Отвечаем отправителю addr.


server.close()
