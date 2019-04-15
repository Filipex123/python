import socket
from random import randint 
# import player
from carta import *


HOST = '127.0.0.1' 
PORT = 65432  
cardList = []

file = open(r"cartas.txt","r")

for line in file.readlines():
    cardList.append(line)
print(cardList)

# print(file.readlines())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))#gera conexao de server
    s.listen()
    
    conn1, addr1 = s.accept()
    conn2, addr2 = s.accept()
    with conn1:
        print('Connected by', addr1)
        while True:
            data = conn1.recv(1024)
            if not data:
                break
            conn1.sendall(data) #manda mensagem para o p1
    
    with conn2:
        print('Connected by', addr2)
        while True:
            data = conn2.recv(1024)
            if not data:
                break
            conn2.sendall(data) #manda mensagem para o p2