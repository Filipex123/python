import socket

HOST = '127.0.0.1'  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))#conecta com o server

    s.sendall(b'Hello, world 2222')
    data = s.recv(1024)#manda mensagem pro server

    print('Received', repr(data))
