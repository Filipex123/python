import re 
from Personagem import * #retirar depois

def filtraString(resp):
    x = re.findall(r'\D+',resp)
    if(len(x)== 0):
        return "Opcao Invalida"
    else:
        return x[0]

def filtraNum(resp,rang):
    x = re.findall(r'\d+',resp)
    if(len(x)== 0 or range(int(x[0]),rang) == False):
        return "Opcao Invalida"
    else:
        return x[0]

def range(num,range):
    if num > range:
        return False
    else:
        return True

def filtraSimOuNao(resp):
    if resp == 'sim':
        return True
    elif resp == 'nao':
        return True
    else:
        return False

