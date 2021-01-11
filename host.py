from puzzle import Puzzle
from wheel import Wheel
from player import Player
from letter_freqs import letters
import time
import os

#Increment ptr 
def incPtr(ptr, numPlayers):
    if ptr == numPlayers - 1:
        ptr = 0
    else: ptr += 1
    return ptr

#Guess handler
def guess(puz, player, spin):
    puz.displayGuessed()
    if player.computer:
        g = player.getComputerGuess(puz.guessed)
    else:
        g = input("Guess a letter: \n")
    num = puz.guess(g, True, player, spin)
    return num == 0

#Spin handler
def spin(wheel, player):
    print('spinning...')
    time.sleep(1)
    spin = wheel.spin()
    player.specialHandle(spin)
    print(spin)
    return spin

#Solve handler
def solve(puz, numPlayers, ptr):
    s = input("Okay go ahead: \n")
    solveCheck = puz.solve(s)
    puz.display()
    if not solveCheck:
         ptr = incPtr(ptr, numPlayers)
    return ptr
    

#A client program to play Wheel from the Command Line
def main():
    #HOST RULES
    print("HOST RULES SELECTION")
    string = input("Choose the secret puzzle: \n")
    os.system('cls')
    size = int(input("Choose wheel size: \n"))
    numBank = int(input("Choose number of bankrupt tiles: \n"))
    numPlayers = int(input("How many players are there? \n"))
    wheel = Wheel(size, numBank*['bankrupt'])
    puz = Puzzle(string)
    os.system('cls')

    ptr = 0
    players = []
    for i in range(1, numPlayers + 1):
        players.append(Player(input("Player " + str(i) + ", enter your name. \n"), False))
    computer = input("Would you like a computer player? [y/n]")
    if computer == 'y': 
        players.append(Player("Computer Player", True))
        numPlayers += 1
    os.system('cls')

    welcome_string = "Welcome  "
    for player in players:
        welcome_string += player.getName() + " "
    print(welcome_string)
    puz.display()

    while not puz.solveCheck():
        print("It's " + players[ptr].getName() + "'s turn!")
        puz.display()
        if not players[ptr].computer:
            ip = input('take a spin! [press enter] or solve [type solve then enter] \n')

            #Handle Solve 
            if ip == 'solve':
                ptr = solve(puz, numPlayers, ptr)
                if puz.solveCheck(): break  

            #Handle Spin
            else:
                spinRet = spin(wheel, players[ptr])
                if spinRet == 'bankrupt':
                    print("Sorry, " + players[ptr].getName() + " you have lost all your money.")
                    ptr = incPtr(ptr, numPlayers)


                #Handle guess
                if type(spinRet) == float:
                    boolGuess = guess(puz, players[ptr], spinRet)
                    if boolGuess:
                        ptr = incPtr(ptr, numPlayers)

        #Handle Computer Player Behavior
        else:
            print("Take a spin! or solve \n")
            time.sleep(1)
            spinRet = spin(wheel, players[ptr])
            time.sleep(1)

            #Computer Spin
            if spinRet == 'bankrupt':
                print("Sorry, " + players[ptr].getName() + " you have lost all your money.")
                ptr = incPtr(ptr, numPlayers)

            #Computer guess
            if type(spinRet) == float:
                    boolGuess = guess(puz, players[ptr], spinRet)
                    if boolGuess:
                        ptr = incPtr(ptr, numPlayers)


        #Print Score
        time.sleep(1)
        print("SCORES")
        for player in players: 
            print(player.getName() + " has " + "$" + str(player.getRMoney()))
        print()
    
    print("Congratulations " + players[ptr].getName() + " you have won " + "$" + str(players[ptr].getRMoney()))

if __name__ == '__main__':
    main()

