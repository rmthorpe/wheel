import random
import time 
from player import Player

class Wheel:
    def __init__(self, size, specials):
        self.__million = True
        self.__wild = True
        self.__trip = True
        self.__specials = len(specials)
        self.__size = size
        self.__tiles = self.setup_tiles(specials)

    def setup_tiles(self, specials):
        money_size = self.__size - self.__specials
        tiles = []     
        for i in range(0, money_size):
            random.seed()
            tiles.append(round(random.uniform(500, 900), -2))
        for s in specials:
            tiles.append(s)
        random.shuffle(tiles)
        return tiles

    def spin(self):
        spin = random.randrange(0, self.__size)
        return self.__tiles[spin]





def main():
    w = Wheel(10,['million', 'wildcard', 'trip'])
    print('take a spin!')
    print('spinning...')
    time.sleep(3)
    print(w.spin())



if __name__ == '__main__':
    main()