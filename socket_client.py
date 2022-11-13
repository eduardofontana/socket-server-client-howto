# Official Documentation
# https://docs.python.org/3.7/howto/sockets.html

import socket


def client_program():
    host = socket.gethostname()  # ambos os códigos estão sendo executados no mesmo pc
    port = 5000  # número da porta do servidor de soquete

    client_socket = socket.socket()  # instanciar
    client_socket.connect((host, port))  # conectar ao servidor

    message = input(" -> ")  # coletar entrada

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # enviar mensagem
        data = client_socket.recv(1024).decode()  # receber resposta

        print('Received from server: ' + data)  # mostrar no terminal

        message = input(" -> ")  # novamente coletar entrada

    client_socket.close()  # fechar conexão


if __name__ == '__main__':
    client_program()

# Gotchaa!

# machinehead$ python3.6 socket_client.py
# -> Hi
# Received from server: Olá
# -> Como vai vc?
# Received from server: Bem
# -> Maravilha!
# Received from server: Ok, então Tchau!
# -> Tchau!
# machinehead$
