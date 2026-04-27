import socket


IPv = socket.AF_INET
SOCK_TYPE = socket.SOCK_STREAM

HOST = "127.0.0.1"
PORT = 8080

CONNECTIONS = 1
CLIENT_TIMEOUT = 3

BASE_CHUNK_SIZE = 1024
FINAL_BYTES = b"\r\n\r\n"


def get_request(conn: socket.socket):
    data = b""
    while not data.endswith(FINAL_BYTES):
        chunk = conn.recv(BASE_CHUNK_SIZE)
        if not chunk:
            return b""
        data += chunk
    return data


def send_response(conn: socket.socket):
    conn.sendall(b"OK!" + FINAL_BYTES)


def handle_connection(conn: socket.socket, addr: tuple):
    try:
        data = get_request(conn)
        print(len(data))
        if not data:
            raise ConnectionError(f"The client {addr} suddenly shut down.")
        send_response(conn)

    except socket.timeout as e:
        print(f"{e}, client - {addr}")
    except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError) as e:
        print(f"Connection with client {addr} was reset...")
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
