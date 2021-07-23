"""
A program where 2 players alternate taking either 1 or 2 stones from a pile of 20 stones
"""

import random

def main():
    stones = 20
    player_num = 1
    while(stones > 0):
        print("There are", str(stones), "stones left")
        stones_got = int(input("Player " + str(player_num) + " would you like to remove 1 or 2 stones? "))
        while (stones_got > 2 or stones_got < 1):
            stones_got = int(input("Please enter 1 or 2: "))
        stones -= stones_got
        if (player_num == 1):
            player_num = 2
        else:
            player_num = 1
        print("")
    print("Player", str(player_num), "wins!")

if __name__ == '__main__':
    main()