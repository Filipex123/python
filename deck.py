class Deck(object):
    
    def __init__(self):
        self.__cards = []
        self.__nome = ''
 
    def setDecksNome(self,nome):
        self.__name = nome

    def getCardsList(self):
        return self.__cards

    def getCardsListToString(self):
        cards_toString = []
        for c in self.__cards:
            cards_toString.append(c.getNome()+"|"+str(c.getAtk())+"|"+str(c.getDef()))
        return cards_toString
    
    def addCard(self,card):
        self.__cards.append(card)
    
    def rmCard(self,card):
        for c in self.__cards:
            if(card.getNome() == c.getNome()):
                self.__cards.remove(c)