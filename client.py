import socket
import pickle

HOST = '127.0.0.1'
PORT = 8080
private_key = 157
public_key = 151
server_public_key = 197

sock = socket.socket()
sock.connect((HOST, PORT))

partial_key = server_public_key ** private_key % public_key

msg = sock.recv(1024)
server_partial_key = pickle.loads(msg)

sock.send(pickle.dumps(partial_key))

full_key = server_partial_key ** private_key % public_key
print('Полный ключ:', full_key)

sock.close()
