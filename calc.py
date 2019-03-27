import re
while True:
    operacao = input("Digite a operacao:")
    if operacao == "exit":
        break
    else:
        sinal = re.findall(r'[+/*-]', operacao)
        n = re.findall(r'\d+', operacao)

        if sinal[0] == '+':
            print (int(n[0])+int(n[1]))
        if sinal[0] == '-':
            print (int(n[0])-int(n[1]))
        if sinal[0] == '*':
            print (float(n[0])*float(n[1]))
        if sinal[0] == '/':
            print (float(n[0])/float(n[1]))

    

