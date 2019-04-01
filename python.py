from time import sleep
from random import randint
from teste import *
from Personagem import *
import re

w = 0
pf = '0'
pag = '1'
pa = '2'
pal = ('1', '2', '3', '4', '5')
fl = randint(1, 5)
idb = randint(0, 1)
vida = 5
tdf = randint(1,8)
s = 'sim'
n = 'nao'
x = False
resp = ''
personagens = 'fogo', 'agua', 'terra'
caminhos = 'direita', 'esquerda', 'frente'
itens =  'bau armadilha', 'vida extra'



print('Bem vindo ao meu jogo')
name = input('Qual o seu nome? ')
print('seja muito bem vindo {}!' .format(name))
sleep(2)
########################################################################
while True:
    resp = str(input('Esta pronto para comecar nossa aventura??? '))
    if resp == 'sim':
########################################################################
        print('Opa chama no xesque, Vamos começar então!!!')
        print('você possui 5 vidas')
        sleep(1)
        print('''Escolha um atributo para seu personagem
        [ 0 ] para personagem de fogo
        [ 1 ] para personagem de agua
        [ 2 ] para personagem de terra''')

 ########################################################################       
        while True:
            resp = filtraNum(input('Qual sera seu personagem? '))
            if(resp != 'Opcao Invalida'):
                person = Personagem(name,personagens[int(resp)])
                break
########################################################################
        sleep(2)
        print('Que comece os jogos')
        print('Voce esta em uma floresta deserta, existem apenas 3 caminhos')
        print('''escolha uma opção de caminho
        [ 0 ] direita
        [ 1 ] esquerda
        [ 2 ] frente''')



        # b = False
        while True:
            resp = filtraString(input('qual caminho você ira seguir '))
            if c == d:
                print('OK, Seguindo para a direita...')
                sleep(3)
                b = True
                print('você encontrou um bau super raro!!!')
                sleep(2)
                c = False
                if w == 0:
                    while c == False:
                        ab = str(input('Deseja abrir esse bau? '))
                        if ab == s:
                            c = True
                            print('OK, abrindo bau...')
                            sleep(3)
                            print('você encontrou um {}' .format(itens[idb]))
                            if itens[idb] == 'bau armadilha':
                                print('voce foi pego pelo bau armadilha!, perca uma vida')
                                vida = vida - 1
                                print('voce esta com {} vidas' .format(vida))
                            elif itens[idb] == 'vida extra':
                                print('você adquiriu uma vida extra, uhuuu!')
                                vida = vida + 1
                                print('você esta com {} vidas' .format(vida))
                        elif ab == n:
                            c = True
                            print('ok, continuando...')
                        else:
                            print('Digite sim ou nao')
                    print('OK, prosseguindo...')
                    sleep(2)
                    print('voce se deparou com uma montanha gigante!! ')
                    print('no topo da montanha possui um vida extra!!')
                    sleep(1)
                    print('porem pode ser perigoso escalar devido ao vento muito forte!')
                    em = str(input('Deseja escalar a montanha? '))
                    d = False
                    while d == False:
                        em = str(input('Deseja escalar a montanha? '))
                        if em == 'sim':
                            d = True
                            print('Ok, escalando...')
                            sleep(2)
                            print('\033[31mPLOFT\033[m')
                            print('voce infelimente caiu devido ao vento...')
                            sleep(2)
                            print('perca uma vida')
                            vida = vida - 1
                            print('voce esta com {} vida(s)' .format(vida))
                            sleep(2)
                            print('vamos dar a volta na montanha...')
                        elif em == 'nao':
                            print('ok vamos dar a volta na montanha entao...')
                            d = True
                        else:
                            print('digite um comando valido')
                    sleep(2)
                    print('voce encontrou um gurreiro alado...')
                    sleep(2)
                    print('nao da pra fugir dos guerreiros alados...')
                    sleep(2)
                    print('sua unica opcao é lutar...')
                    sleep(2)
                    print('\033[31mEscolha um numero de 1 a 5\033[m')
                    print('esses numeros sao sorteados aleatoriamente')
                    print('voce tera 2 palpites, se acertar ganhará a luta!')
                    f = False
                    while f == False:
                        b5 = re.findall(r'\d+', input('Digite seu primeiro palpite '))
                        b6 = re.findall(r'\d+', input('Digite seu segundo palpite '))
                        if b5 and b6 == int:
                            if b5 == fl3:
                                print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                                print('o adversario escolheu o numero {}'.format(fl3))

                            elif b6 == fl3:
                                print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                                print('o adversario escolheu o numero {}'.format(fl3))

                            else:
                                print('VOCE PERDEEUUUUU')
                                print('o adversario escolheu o numero {}, perca uma vida'.format(fl3))
                                vida = vida - 1
                                print('voce esta com {} vida(s)' .format(vida))
                                sleep(2)
                        else:
                            print('digite um comando valido')

                    print('Continuando aventura...')
                    sleep(4)
                    print('O que é aquilo na frente??')
                    sleep(2)
                    print('um brilho muito forte')
                    k = False
                    #ARRUMAR A PARTIR DAQUI:
                    while k == False:
                        e4 = str(input('Deseja seguir '))
                        if e4 == 'sim':
                            k = True
                            print('OK, Vamos chegar mais perto...')
                            sleep(5)
                            print('ainda nao da pra ver, mais perto...')
                            sleep(3)
                            print('\033[31mOH NAO\033[m')
                            sleep(1)
                            print('VOCE ENCONTROU UM GUERREIRO PALADINO BRILHOSO...')
                            sleep(1)
                            print('se voce batalhar e ganhar, ganhara um palpite a mais nas lutas...')
                            sleep(2)
                            print('porem se perder, perdera duas vidas...')
                            sleep(2)
                            h = False
                            while h == False:
                                e5 = str(input('deseja lutar com o \033[35mGUERREIRO PALADINO ALADO\033[m? '))
                                if e5 == 'sim':
                                    h = True
                                    print('\033[31mQUE COMECE A LUTA!!!\033')
                                    sleep(2)
                                    print('\033[31mEscolha um numero de 1 a 5\033[m')
                                    print('esses numeros sao sorteados aleatoriamente')
                                    print('voce tera 2 palpites, se acertar ganhará a luta!')
                                    g = False
                                    while g == False:
                                        b7 = input('Digite seu primeiro palpite ')
                                        b8 = input('Digite seu segundo palpite ')
                                        if b7 == int:
                                            print('Digite um comando valido')
                                        elif b8 == int:
                                            print('digite um comando valido')
                                        else:
                                            g = True
                                            if b7 == fl2:
                                                print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                                                print('o adversario escolheu o numero {}'.format(fl2))
                                            elif b8 == fl2:
                                                print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                                                print('o adversario escolheu o numero {}'.format(fl2))
                                            else:
                                                print('VOCE PERDEEUUUUU')
                                                print('o adversario escolheu o numero {}, perca uma vida'.format(fl2))
                                                vida = vida - 1
                                                print('voce esta com {} vida(s)'.format(vida))
                                                sleep(2)
                                elif e5 == 'nao':
                                    print('ok, vamos dar a volta para o guerreiro nao nos ver...')
                                    h = True
                                else:
                                    print('digite um comando valido')


                        elif e4 == 'nao':
                            print('ok, vamos evitar o brilho...')
                            k = True
                            sleep(2)
                        else:
                            print('Digite um Comando Valido')



                    #continuar aqui::


                else:
                    print('ok tchau')

            elif c == e:
                b = True
                print('OK, seguindo pra esquerda...')
                sleep(3)
                print('Voce encontrou um guerreiro de agua...')
                sleep(2)
                e2 = str(input('Deseja tentar fugir? ou quer lutar? '))
                if e2 == 'fugir':
                    print('Voce esta tentando fugir...')
                    sleep(2)
                    if tdf % 2 == 1:
                        print('Voce conseguiu fugir!!! parabens!!')
                    elif tdf % 2 == 0:
                        print('o guerreiro de agua usou jato tsunami enquanto voce estava fungindo')
                        print('Perca uma vida')
                        vida = vida - 1
                        print('voce esta com {} vidas' .format(vida))
                else:
                    print('\033[31mEscolha um numero de 1 a 5\033[m')
                    print('esses numeros sao sorteados aleatoriamente')
                    print('voce tera 2 palpites, se acertar ganhará a luta!')
                    b3 = int(input('Digite seu primeiro palpite '))
                    b4 = int(input('Digite seu segundo palpite '))
                    if b3 == fl:
                        print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                        print('o adversario escolheu o numero {}'.format(fl))
                    elif b4 == fl:
                        print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                        print('o adversario escolheu o numero {}'.format(fl))
                    else:
                        print('VOCE PERDEEUUUUU')
                        print('o adversario escolheu o numero {}'.format(fl))
                        print('perca uma vida')
                        vida = vida - 1
                        print('voce esta com {} vida(s)' .format(vida))
                print('prosseguindo aventura...')
                sleep(3)
                print('que barulho é esse vindo do ceu??')
                sleep(3)
                print('TEM UM METEORO CAINDO!!!!...')
                sleep(2)
                print('ELE ESTA INDO EM SUA DIREÇÃO!!!!!!!')
                print('CORREEEE.......')
                sleep(4)
                print('\033[31mBBBBBBUUUUUUUUUMMMMMMMMMMMMM\033[m')
                sleep(2)
                print('ufa foi por pouco')
                sleep(2)
                print('quase que ele te atingiu...')
                sleep(2)
                print('que estranho esse meteoro tem uma cor vermelha')
                sleep(2)
                y = False
                while y == False:
                    m = str(input('Deseja se aproximar? '))
                    if m == 'sim':
                        y = True
                        print('ok vamos nos aproximar...')
                        sleep(3)
                        print('Parece que tem um brilho \033[31mVERMELHO!!\033[m...')
                        sleep(3)
                        print('O QUE É ISSO????????')
                        sleep(2)
                        print('A LUZ VERMELHA ESTA TE CONSUMINDO....')
                        sleep(1)
                        print('...')
                        sleep(2)
                        print('...')
                        sleep(3)
                        print('\033[31mVOCE ADIQUIRIU UM PODER SOMBRIOO\033[m')
                        sleep(3)
                        print('\033[31mAGORA VOCE TEM UM PODER SUPREMO SOMBRIO BUAHAHHAA\033[m')
                        sleep(3)
                        print('\033[31mVOCE TERA 4 PALPITES NAS LUTAS POR CAUSA DE SEU NOVO PODER\033[m')
                        v = v + 2
                        sleep(3)
                        print('\033[31mVAMOS CONTINUAR A AVENTURA...\033[m')
                        sleep(2)
                    elif m == 'nao':
                        y = True
                        print('ok nao vamos arriscar...')
                        sleep(3)
                    else:
                        print('digite um comando valido')
                #CONTINUAR AQUI::
                print('Vamos seguir em frente...')

            elif c == f:
                b = True
                print('OK seguindo para frente')
                sleep(3)
                print('voce encontrou um guerreiro de fogo!!')
                e3 = str(input('Deseja tentar fugir? ou quer lutar contra o bunda mole?'))
                if e3 == 'fugir':
                    print('Voce esta tentando fugir...')
                    sleep(2)
                    if tdf1 % 2 == 1:
                        print('Voce conseguiu fugir!!! parabens!!')
                    elif tdf1 % 2 == 0:
                        print('o guerreiro de agua usou jato tsunami enquanto voce estava fungindo')
                        print('Perca uma vida')
                        vida = vida - 1
                        print('voce esta com {} vidas'.format(vida))
                else:
                    print('\033[31mEscolha um numero de 1 a 5\033[m')
                    print('esses numeros sao sorteados aleatoriamente')
                    print('voce tera 2 palpites, se acertar ganhará a luta!')
                    if v == 0:
                        b1 = int(input('Digite seu primeiro palpite '))
                        b2 = int(input('Digite seu segundo palpite '))
                        if b1 == fl1:
                            print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                            print('O adversario escolheu o numero {}' .format(fl1))
                        elif b2 == fl1:
                            print('\033[33mPARABÉNS!!! VOCE GANHOU!!!\033[m')
                            print('O adversario escolheu o numero {}' .format(fl1))
                        else:
                            print('VOCE PERDEEUUUUU')
                            print('o adversario escolheu o numero {}' .format(fl1))
                            print('pc = {}'.format(fl1))
            else:
                print('Digite um caminho valido')
    elif e1 == 'nao':
        print('ok, voce nao esta pronto ainda')
        x = True
    else:
        print('Digite sim ou nao xupingole')
