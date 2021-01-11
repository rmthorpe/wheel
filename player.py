from letter_freqs import letters
import random
class Player:

    def __init__(self, name, computer):
        self.__name = name
        self.__roundMoney = 0
        self.__gameMoney = 0
        self.computer = computer
        self.computerPtr = 0
    
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

    def getComputerGuess(self, guessed):
        letterByFreq = list(letters.keys())
        nums = range(0, 26)
        distrib = letters.values()
        guess = letterByFreq[random.choices(nums, distrib)[0]]
        while len({guess}.intersection(guessed)) > 0:
            self.computerPtr += 1
            guess = letterByFreq[random.choices(nums, distrib)[0]]
        print(guess)
        return guess


