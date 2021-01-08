from puzzle import Puzzle 

def setup():
    string = input("Choose the secret puzzle: \n")
    puz = Puzzle(string)
    while not puz.solveCheck():
        g = input("Guess a letter or solve [type solve]: \n")
        if g != 'solve':
            puz.guess(g)
            puz.display()
        else:
            s = input("Okay go ahead: \n")
            puz.solve(s)
            puz.display()

def main():
    setup()

if __name__ == '__main__':
    main()

