#CodeRefectoring
from time import sleep
from random import randint
from Personagem import *

heroi = Personagem()
resp = ""

print('Bem vindo ao meu jogo')
nome = input('Qual o seu nome? ')
heroi.setNome(nome)
print('seja muito bem vindo {}!' .format(heroi.getNome()))
sleep(2)

while True:
    resp = input('Esta pronto para comecar nossa aventura??? ')
    if(resp == 'sim'):
        break
    elif(resp == 'nao'):
        print("See you next time")
        sleep(2)
        exit()

print('bora la')