import socket
from deck import *
from random import randint 
# import player
from carta import *


HOST = '127.0.0.1' 
PORT = 65432  
deck1 = Deck()
deck2 = Deck()
decks = [deck1,deck2]
file = open(r"cartas.txt","r")


for x in file.readlines():
    x_info = x.split("/")
    n = randint(0,1)
    decks[n].addCard(Carta(x_info[0],x_info[1],x_info[2][0:len(x_info[2])-1]))
print(decks[0].getCardsListToString())
print(decks[1].getCardsListToString())
# for line in file.readlines():
#     n = randint(0,1)
#     cinfo = line.split("/")

#     if n == 0 and cont1 < 5:
#         cont1 +=1
#         deck1.addCard(Carta(cinfo[0],cinfo[1],cinfo[2]))
#     elif n == 1 and cont2 < 5:
#         cont2 +=1
#         cardList2.append(Carta(cinfo[0],cinfo[1],cinfo[2]))
    
# print(cardList[1].getNome())
# print(file.readlines())
file.close()


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