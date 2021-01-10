#A client program to play Wheel from the Command Line

from puzzle import Puzzle
from wheel import Wheel
from player import Player
import time
import os

def main():
    string = input("Choose the secret puzzle: \n")
    wheel = Wheel(10, ['bankrupt'])
    puz = Puzzle(string)
    os.system('cls')
    player_name = input("Player 1, enter your name. \n")
    os.system('cls')

    print("Welcome " + player_name)
    player = Player(player_name)
    puz.display()

    while not puz.solveCheck():
        ip = input('take a spin! [press enter] or solve [type solve then enter] \n')

        #Handle Solve 
        if ip == 'solve':
            s = input("Okay go ahead: \n")
            puz.solve(s)
            puz.display()
            if puz.solveCheck(): break 

        #Handle Spin
        else: 
            print('spinning...')
            time.sleep(1)
            spin = wheel.spin()
            player.specialHandle(spin)
            print(spin)

        #Handle guess
        if type(spin) == float:
            g = input("Guess a letter: \n")
            num = puz.guess(g)
            player.incRMoney(num * spin)
            puz.display()

        #Print Score
        print(player.getName() + " has " + "$" + str(player.getRMoney()))
    
    print("Congratulations " + player.getName() + " you have won " + "$" + str(player.getRMoney()))

if __name__ == '__main__':
    main()

