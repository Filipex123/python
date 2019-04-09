#CodeRefectoring
from time import sleep
from random import randint
from Personagem import *
from functions import *

heroi = Personagem()
resp = ""
vet_atributos = 'fogo', 'agua', 'terra'
caminhos = 'direita','esquerda','frente'
trilha = []

print('Bem vindo ao meu jogo')
nome = input('Qual o seu nome? ')
heroi.setNome(nome)
print('seja muito bem vindo {}!' .format(heroi.getNome()))
# sleep(2)

while True:
    resp = input('Esta pronto para comecar nossa aventura??? ')
    if(resp == 'sim'):
        break
    elif(resp == 'nao'):
        print("See you next time")
        sleep(2)
        exit()

print('bora la')
print('Opa chama no xesque, Vamos começar então!!!')
print('você possui 5 vidas')
# sleep(1)
print('''Escolha um atributo para seu personagem
[ 0 ] para personagem de fogo
[ 1 ] para personagem de agua
[ 2 ] para personagem de terra''')

while True:
    resp = filtraNum(input('Qual sera seu personagem? '))
    if(resp != 'Opcao Invalida'):
        heroi.setAtributo(vet_atributos[int(resp)])
        break

# sleep(2)
print('Que comece os jogos')
print('Voce esta em uma floresta deserta, existem apenas 3 caminhos')
print('''escolha uma opção de caminho
     [ 0 ] direita
     [ 1 ] esquerda
     [ 2 ] frente''')

while True:
    resp = filtraNum(input('qual caminho você ira seguir '))
    if(resp != 'Opcao Invalida'):
        trilha.append(caminhos[int(resp)])
        break

if(trilha.pop() == 'direita'):############FLUXO DA TRILHA DA DIREITA ######
    print('OK, Seguindo para a direita...')
    # sleep(3)
    print('você encontrou um bau super raro!!!')
    # sleep(2)

    while True: ############### FLUXO BAU ##################
        resp = filtraString(input('Deseja abrir esse bau? '))
        if(resp != 'Opcao Invalida' and  resp == 'sim'):
            print('OK, abrindo bau...')
            # sleep(3)
            n_sort = randint(0,1)
            if n_sort == 0:
                print('voce foi pego pelo bau armadilha!, perca uma vida')
                heroi.dano(1)
                print('voce esta com {} vidas' .format(heroi.getVida()))
            else:
                print('você encontrou uma poção de vida extra, uhuuu!')
                heroi.cura(1)
                print('você esta com {} vidas' .format(heroi.getVida()))
            break

    print("Prosseguindo...")
    # sleep(2)
    print('voce se deparou com uma montanha gigante!! ')
    print('no topo da montanha possui um vida extra!!')
    # sleep(1)
    print('porem pode ser perigoso escalar devido ao vento muito forte!')


    while True: ############### FLUXO MONTANHA ##################
        resp = filtraString(input('Deseja escalar a montanha? '))
        if(resp != 'Opcao Invalida' and  resp == 'sim'):
            print('Ok, escalando...')
            #sleep(2)
            print('voce infelimente caiu devido ao vento...')
            # sleep(2)
            print('perca uma vida')
            heroi.dano(1)
            print('voce esta com {} vida(s)' .format(heroi.getVida))
            # sleep(2)
            print('vamos dar a volta na montanha...')
        else:
            print('você encontrou uma poção de vida extra, uhuuu!')
            heroi.cura(1)
            print('você esta com {} vidas' .format(heroi.getVida()))
        break

    