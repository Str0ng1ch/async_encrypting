import socket
import pickle

HOST = '127.0.0.1'
PORT = 8080
private_key = 199
public_key = 197
client_public_key = 151

print('запуск сервера')
sock = socket.socket()  # Создание сокета

sock.bind((HOST, PORT))  # связывание сокета с хостом и портом

sock.listen(1)  # запуск режима прослушивания порта
print('Начало прослушивания порта')
conn, addr = sock.accept()  # Принимаем подключение с помощью метода accept
print('Клиент подключен', addr)


partial_key = public_key ** private_key % client_public_key

conn.send(pickle.dumps(partial_key))

msg = conn.recv(1024)
client_partial_key = pickle.loads(msg)

full_key = client_partial_key ** private_key % client_public_key
print('Полный ключ:', full_key)

conn.close()
