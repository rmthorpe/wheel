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
        self.__vowels = set(string).intersection(set('aeiou'))

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

    #Handle letter guesses and fill out in process string
    def guess(self, char):
        char = char.lower()
        getVal = self.__freq.get(char)
        if getVal == None:
            print('Sorry, no ' + char.upper() + 's')
        else:
            print('Yes, ' + str(getVal) + ' ' + char.upper() +'s')
            position = self.__pos.get(char)
            for p in position:
                self.__blank[p] = char.upper()
                self.__corSoFar += 1
                if self.__corSoFar == self.__numChars:
                    self.__isSolved = True

    #Attempt to solve the puzzle
    def solve(self, string):
        if string.lower() == self.__puzzle_string.lower():
            print("You got it!")
            self.__isSolved = True
        else:
            print("Sorry, no.")

    #Display the in process puzzle string
    def display(self): 
        if self.__isSolved:
            print(self.__puzzle_string.upper())
        else:
            string = ''
            for a in self.__blank:
                string += a
            print(string) 

#For testing
def main():
    puz = Puzzle("Ryan")
    puz.display()
    puz.guess('r')
    puz.display()
    puz.solve('RyAn')
    puz.display()

if __name__ == '__main__':
    main()
