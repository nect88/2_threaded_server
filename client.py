import socket
import logging as log

log.basicConfig(filename='client.txt', level=log.DEBUG)


def send(conn, message):
    header = len(message)
    full_message = f'{header:4}{message}'.encode()
    conn.send(full_message)


def receive(conn):
    header = conn.recv(4).decode()
    message = conn.recv(int(header))
    return message.decode()


def identify(sock):
    data = receive(sock)
    if data == 'Как вас зовут?':
        name = input(data)
        send(sock, name)
        data = receive(sock)
    print(data)


sock = socket.socket()
log.info('Запуск клиента')
port = int(input('port.py: '))
sock.connect(('localhost', port))
log.info('Подключен к серверу')
identify(sock)
msg = ''
while msg != 'exit':
    msg = input()
    log.info('Отправка сообщения {}'.format(msg))
    send(sock, msg)
    log.info('Получение ответа от сервера')
    received_msg = receive(sock)
    print(received_msg)
sock.close()
