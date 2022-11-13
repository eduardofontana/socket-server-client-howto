# Official Documentation
# https://docs.python.org/3.7/howto/sockets.html

import socket


def server_program():
    # obter o nome do host
    host = socket.gethostname()
    port = 5000  # iniciar a porta abaixo de 1024

    server_socket = socket.socket()  # obter instância
    # A função bind() recebe tupla como argumento
    server_socket.bind((host, port))  # vinculando o endereço do host e a porta juntos

    # configurar quantos clientes o servidor pode escutar simultaneamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # aceitar nova conexão
    print("Connection from: " + str(address))
    while True:
        # recebe fluxo de dados, não aceitará pacotes de dados maiores que 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # se os dados não forem recebidos hávera pausa
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # enviar dados para o cliente

    conn.close()  # fechar conexão


if __name__ == '__main__':
    server_program()

# Gotchaa!

# machinehead$ python3.6 socket_server.py
# Connection from: ('127.0.0.1', 57822)
# from connected user: Oi
# -> Olá
# from connected user: Como vai vc?
# -> Bem
# from connected user: Maravilha!
# -> Ok, então Tchau!
# machinehead$