import re 

def filtraString(resp):
    x = re.findall(r'\D+',resp)
    if(len(x)== 0):
        return "Opcao Invalida"
    else:
        return x[0]

def filtraNum(resp):
    x = re.findall(r'\d+',resp)
    if(len(x)== 0 or int(x[0])>2):
        return "Opcao Invalida"
    else:
        return x[0]



print(filtraString('1231'))