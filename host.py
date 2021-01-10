from puzzle import Puzzle
from wheel import Wheel
import time
import os

def setup():
    string = input("Choose the secret puzzle: \n")
    wheel = Wheel(10, ['million', 'wildcard', 'trip'])
    puz = Puzzle(string)
    os.system('cls')
    while not puz.solveCheck():
        print('take a spin! [press s then enter to spin]')
        while input() != 's': continue
        print('spinning...')
        time.sleep(1)
        print(wheel.spin())
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

