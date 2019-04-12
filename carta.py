class Carta(object):

    def __init__(self,nome,ataque,defesa):
        self.__nome = nome
        self.__ataque = ataque
        self.__defesa = defesa

    
    def getNome(self):
        return self.__nome

    def getAtk(self):
        return self.__ataque

    def getDef(self):
        return self.__defesa