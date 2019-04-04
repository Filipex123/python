class Personagem(object):

    def __init__(self):
        self.__vida = 5 
        self.__nome = ""


    def getVida():
        return self.__vida

    def setNome(self,nome):
        self.__nome = nome    

    def getNome(self):
        return self.__nome 

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
