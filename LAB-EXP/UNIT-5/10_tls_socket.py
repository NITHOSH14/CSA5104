import socket, ssl

HOST = 'localhost'
PORT = 8443


def server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('server.crt', 'server.key')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, _ = ssock.accept()
            data = conn.recv(1024)
            print('Server received:', data.decode())
            conn.sendall(b'Connected with TLS')


def client():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            ssock.sendall(b'Hello TLS')
            print('Client got:', ssock.recv(1024).decode())


if __name__ == '__main__':
    print('Generate certificate first using 12_generate_self_signed_cert.py')
