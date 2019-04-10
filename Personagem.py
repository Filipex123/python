class Personagem(object):

    def __init__(self):
        self.__vida = 5 
        self.__nome = ""
        self.__atributo = ""


    def getVida(self):
        return self.__vida

    def setNome(self,nome):
        self.__nome = nome    

    def getNome(self):
        return self.__nome 

    def getAtributo(self):
        return self.atributo   

    def setAtributo(self,atributo):
         self.__atributo = atributo

    def dano(self,qtd):
        if (self.__vida - qtd >=0):
            self.__vida -= qtd
        else:
            print("Voce esta morto")

    def cura(self,qtd):
        self.__vida += qtd  
