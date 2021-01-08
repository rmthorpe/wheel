class puzzle:

    #Initialize the puzzle object
    def __init__(self, string):
        self.puzzle_string = string
        self.dict = self.freqParse(string)
        self.vowels = set(string).intersection(set('aeiou'))

    #Convert the puzzle string into a dictionary of letters with their frequency
    def freqParse(self, string):
        d = dict()
        for char in string:
            check = d.get(char)
            if check is None:
                d[char] = 1
            else:
                d[char] += 1
        return d

    #Convert the puzzle string into a dictionary of letters with their position

def main():
    puz = puzzle("hello")
    print(puz.dict)

if __name__ == '__main__':
    main()
