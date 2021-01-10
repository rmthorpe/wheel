class Player:

    def __init__(self, name):
        self.__name = name
        self.__roundMoney = 0
        self.__gameMoney = 0
    
    def getName(self):
        return str(self.__name)

    def getRMoney(self):
        return self.__roundMoney

    def getGMoney(self):
        return self.__gameMoney

    def incRMoney(self, amt):
        self.__roundMoney += amt

    def incGMoney(self, amt):
        self.__gameMoney += amt

    def specialHandle(self, spin):
        if type(spin) != float:
            if spin == 'bankrupt':
                self.__roundMoney = 0
