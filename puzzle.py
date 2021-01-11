class Puzzle:

    #Initialize the puzzle object
    def __init__(self, string):

        #Puzzle and display string
        self.__puzzle_string = string
        self.__blank = self.blanks(string)

        #Helper dictionaries and counters
        temp = self.parse(string)
        self.__numChars = temp[2]
        self.__corSoFar = 0
        self.__freq = temp[0]
        self.__pos = temp[1]
        self.guessed = dict()
        self.__vowels = set(string).intersection({'a', 'e', 'i', 'o', 'u'})
        self.__allVowels = {'a', 'e', 'i', 'o', 'u'}

        #Checks
        self.__isSolved = False

    def solveCheck(self):
        return self.__isSolved

    #Convert the puzzle string into a dictionary of letters with their frequency 
    # and a dictionary of letters with their position
    def parse(self, string):
        d = dict()
        pos = dict()
        total = 0
        i = 0
        for char in string:
            char = char.lower()
            check = d.get(char)
            if check is None:
                if char.isalpha():
                    total += 1
                    d[char] = 1
                    pos[char] = [i]
            else:
                if char.isalpha():
                    total += 1
                    d[char] += 1
                    pos[char].append(i)
            i += 1
        return (d, pos, total)

    #Create the blanks of the puzzle string
    def blanks(self, string):
        blanks = []
        for char in string:
            char = char.lower()
            if char == ' ':
                blanks.append('  ')
            elif char == "'":
                blanks.append("' ")
            else:
                blanks.append('_ ')
        return blanks

    #Check for no more vowels
    def vowel(self, char):
        intersect = {char}.intersection(self.__vowels)
        if len(intersect) == 1:
            self.__vowels.remove(char)
            if len(self.__vowels) == 0:
                print("NO MORE VOWELS")

    #Guess a char
    def charGrab(self, char):
        self.guessed[char] = True
        position = self.__pos.get(char)
        self.vowel(char)
        for p in position:
            self.__blank[p] = char.upper() + ' '
            self.__corSoFar += 1
            if self.__corSoFar == self.__numChars:
                self.__isSolved = True

        return len({char}.intersection({'a', 'e', 'i', 'o', 'u'})) > 0

    #Handle letter guesses and fill out in process string
    def guess(self, char, firstguess, player, spin):
        char = char.lower()
        getVal = self.__freq.get(char)
        already = self.guessed.get(char)

        if firstguess == True and len({char}.intersection(self.__allVowels)) > 0:
            if not player.computer:
                char = input("You need to guess a consonant first: \n")
                return self.guess(char, True, player, spin)
            else:
                player.computerPtr += 1
                return self.guess(player.getComputerGuess(self.guessed), True, player, spin)

        else:
            if already != None:
                print("Oh sorry, you already guessed " + char.upper())
                return 0

            else:   
                if getVal == None:
                    print('Sorry, no ' + char.upper() + 's')
                    self.guessed[char] = True
                    return 0

                else:
                    print('Yes, ' + str(getVal) + ' ' + char.upper() +'s')
                    isVowel = self.charGrab(char)
                    self.display()
                    if not isVowel:
                        player.incRMoney(getVal * spin)
                    
                    if not player.computer:
                        if player.getRMoney() > 250.0 and len(self.__vowels) > 0: 
                            vowel = input("Buy a vowel? (Vowels cost $250) [a/e/i/o/u or n]")
                            while len({vowel}.intersection({'a', 'e', 'i', 'o', 'u', 'n'})) < 0:
                                vowel = input("Invalid input. Accepted characters [a/e/i/o/i or n]")
                            if vowel == 'n':
                                return
                            else:
                                player.incRMoney(-250)
                                return self.guess(vowel, False, player, spin)
                    return 1

    #Attempt to solve the puzzle
    def solve(self, string):
        if string.lower() == self.__puzzle_string.lower():
            print("You got it!")
            self.__isSolved = True
            return True
        else:
            print("Sorry, no.")
            return False

    #Display the in process puzzle string
    def display(self): 
        if self.__isSolved:
            print(self.__puzzle_string.upper())
        else:
            string = ''
            for a in self.__blank:
                string += a
            print(string)

    def displayGuessed(self):
        print('Letters guessed: ' + str(sorted(self.guessed)))

#For testing
def main():
    print("HI")

if __name__ == '__main__':
    main()
