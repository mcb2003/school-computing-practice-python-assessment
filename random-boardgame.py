#!/usr/bin/env python3
#random-boardgame   -   the most random boardgame made for a school project
#    Copyright (C) 2017  Michael C Buchan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    email:  mikeybuchan@hotmail.co.uk

#import the random module for rolling the dice
import random

#create the main board class
class game(object):
    def __init__(self,confpath="./random-boardgame.conf"):
        self.board = "43   44   45   46   47   48   49\n\n42   41   40   39   38   37   36\n\n29   30   31   32   33   34   35\n\n28   27   26   25   24   23   22\n\n15   16   17   18   19   20   21\n\n14   13   12   11   10   09   08\n\n01   02   03   04   05   06   07"
        self.confpath = confpath
        self.playerdice = [[0,0],[0,0]]
        self.playerpos = [0,0]
        self.obstacles = [[],[]]
        self.load_obstacles()
        self.start_game()
    
    def start_game(self):
        print("Welcome to Random BoardGame! In this game, you play against an aponent, rolling two dice. If those dice turn out to be the same, say gouldbye to your awesome score, because points will be taken. Otherwise, however, the dice will be added and this will be added to your score, moving you up the board. The first to reach 49 wins. Good luck!\nCopyright (C) 2017  Michael C Buchan\nboard:")
        print(self.board)
        self.won = False
        while self.won==False:
            for player in range(2):
                self.roll_dice(player+1)
    
    def roll_dice(self,player):
        for i in range(2):
            dice = random.randint(1,6)
            self.playerdice[player-1][i] = dice
        print("Player", player, "got a", self.playerdice[player-1][0], "and a", self.playerdice[player-1][1], "!")
        if self.playerpos[0]>=49:
            self.player_win(0)
        elif self.playerpos[1]>=49:
            self.player_win(1)
        if self.playerdice[player-1][0]==self.playerdice[player-1][1]:
            print("Oh no! Looks like we have a double. Sorry, go back", dice, "spaces.")
            self.playerpos[player-1] -= dice
        else:
            total = self.playerdice[player-1][0] + self.playerdice[player-1][1]
            self.playerpos[player-1] += total
        if self.playerpos[player-1]<=0:
            self.playerpos[player-1] = 0
        if self.playerpos[player-1] in self.obstacles[0]:
            index = self.obstacles[0].index(self.playerpos[player-1])
            spaces = self.obstacles[1][index]
            print("It appears we've hit an obstacl. You can now go forward/back ", spaces, " spaces.")
            self.playerpos[player-1] += int(spaces)
        print("You are now on space", self.playerpos[player-1])
        input("Press enter to continue: ")
    
    def player_win(self,player):
        print("Player", player, "has won! Congratulations!")
        user_in = input("Play again? y/N? ").lower()
        if user_in=="y":
            self.playerpos = [0,0]
        else:
            self.won = True
            exit(0)
    
    def load_obstacles(self):
        self.confile = open(self.confpath,'r')
        self.conftext = self.confile.read()
        self.conftext = self.conftext.split("\n")
        for line in self.conftext:
            obstpos = line.split(" ")[0]
            obstspaces = line.split(" ")[1]
            self.obstacles[0].append(obstpos)
            self.obstacles[1].append(obstspaces)
        #print(self.obstacles[0])
        #print(self.obstacles[1])

boardgame = game()