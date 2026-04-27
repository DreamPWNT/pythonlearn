import socket
import time

HOST = "127.0.0.1"
PORT = 8081

# SOCK_DGRAM - сокет с протоколом UDP.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)
while True:
    # Пишем всегда с указанием кому в методе sendto.
    sock.sendto(b"Hello", (HOST, PORT))
    try:
        data, addr = sock.recvfrom(1024)
        # Обычно это используется как одиночные запросы.
        # Постоянного диалога нет, получили 1 ответ и всё.
        if data:
            break
    except socket.timeout:
        print("Not response.")
        time.sleep(2)
        
sock.close()

print(data)