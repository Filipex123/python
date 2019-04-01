class Personagem:

    def __init__(self,nome,atributo):
        self.vida = 5


    def getVida():
        return self.vida

    def setNome(nome):
        self.nome = nome    
    def getNome():
        return self.nome 

    def getAtributo():
        return self.atributo   
    def setAtributo(atributo):
         self.atributo = atributo

    def dano(qtd):
        if self.vida - qtd >=0:
            self.vida -= qtd
        else:
            print("Voce esta morto")

    def cura(qtd):
        self.vida += qtd  
