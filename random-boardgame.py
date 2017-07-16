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
    #define the __init__ function for initialising the program
    def __init__(self,confpath="./random-boardgame.conf"):
        #define the board  variable containing the board layout
        self.board = "43   44   45   46   47   48   49\n\n42   41   40   39   38   37   36\n\n29   30   31   32   33   34   35\n\n28   27   26   25   24   23   22\n\n15   16   17   18   19   20   21\n\n14   13   12   11   10   09   08\n\n01   02   03   04   05   06   07"
        #make it easier to access the confpath variable by incorporating it into the class object itself
        self.confpath = confpath
        #create a multi-dimentional array to storing the player dice rolls
        self.playerdice = [[0,0],[0,0]]
        #define a variable to store the position of the players
        self.playerpos = [0,0]
        #create an empty array to store the obstacles. This is multi-dimentional to store the position of the obstacle and the number of spaces it moves the player
        self.obstacles = [[],[]]
        #call the function to  read the obstacles from the config file
        self.load_obstacles()
        #call the start_game function to loop through the players, calculating their new positions until someone gets past 49 when the game ends
        self.start_game()
    
    #define the start_game function, used as the main function to loop through the players
    def start_game(self):
        #print the welcome message and copyright
        print("Welcome to Random BoardGame! In this game, you play against an aponent, rolling two dice. If those dice turn out to be the same, say gouldbye to your awesome score, because points will be taken. Otherwise, however, the dice will be added and this will be added to your score, moving you up the board. The first to reach 49 wins. Good luck!\nCopyright (C) 2017  Michael C Buchan\nboard:")
        #output the board to the screen so that the players can get a feel for the game
        print(self.board)
        #set a variable to tell us if the game is won or not. This is used to stop the main loop
        self.won = False
        #loop for ever until the game is won
        while self.won==False:
        #loop through the two players constantly
            for player in range(2):
        #call the roll_dice function to generate the dice numbers and check the score against some conditions
                self.roll_dice(player+1)
    
    #define the roll_dice function to generate the dice rolls and check the scores
    def roll_dice(self,player):
        generate two dice numbers
        for i in range(2):
            #actually generate the dice number
            dice = random.randint(1,6)
            #store the dice rolls in the correct location in the playerdice function
            self.playerdice[player-1][i] = dice
        #output the scores to the screen
        print("Player", player, "got a", self.playerdice[player-1][0], "and a", self.playerdice[player-1][1], "!")
        #check if this player or the other player has won the game yet
        if self.playerpos[0]>=49:
            #call the player_win function to win and end the game if the user specifies
            self.player_win(0)
        #check if the other player has won
        elif self.playerpos[1]>=49:
            #if so, win the game with the other player
            self.player_win(1)
        #check if we have a double score
        if self.playerdice[player-1][0]==self.playerdice[player-1][1]:
            #tell the user that they have hit a double score and will move back
            print("Oh no! Looks like we have a double. Sorry, go back", dice, "spaces.")
        #actually move the player
            self.playerpos[player-1] -= dice
        #otherwise
        else:
            #calculate the ammount of spaces to move forward
            total = self.playerdice[player-1][0] + self.playerdice[player-1][1]
            #move the player forward the total number of spaces
            self.playerpos[player-1] += total
        #check to see if this will make the player go back to less than 0
        if self.playerpos[player-1]<=0:
            #if this happens, set the playerpos to the lowest number on the game board, 1
            self.playerpos[player-1] = 1
        #check to see if we have an obstacle
        if self.playerpos[player-1] in self.obstacles[0]:
            #get the index of the ammount of spaces to move
            index = self.obstacles[0].index(self.playerpos[player-1])
        #actually get the ammount of spaces to move
            spaces = self.obstacles[1][index]
            #tell the user that we've hit an obstacle
            print("It appears we've hit an obstacle. You can now go forward/back ", spaces, " spaces.")
            #move the player to the correct place, taking into account the obstacles
            self.playerpos[player-1] += int(spaces)
        #tell the user what space they are now on
        print("You are now on space", self.playerpos[player-1])
        #hold the program until the user  presses the enter key
        input("Press enter to continue: ")
    
    #define the player_win function for winning the game
    def player_win(self,player):
        #tell the players that one of them has won
        print("Player", player, "has won! Congratulations!")
        #ask the players if they want to play again
        user_in = input("Play again? y/N? ").lower()
        #check to see if they said yes or no
        if user_in=="y":
        #reset the player position
            self.playerpos = [0,0]
        #if they said no:
        else:
            #set the won variable to true to stop the loop
            self.won = True
            #exit the program with exit status 0
            exit(0)
    
    #define the load_obstacles
    def load_obstacles(self):
        #create the file object to read the config file
        self.confile = open(self.confpath,'r')
        #get the text from the file
        self.conftext = self.confile.read()
        #split the text into lines
        self.conftext = self.conftext.split("\n")
        #loop through the lines
        for line in self.conftext:
            #split the line into words to read individual fields. Then set the obstacle position to the first field
            obstpos = line.split(" ")[0]
            #set the second field to the amount of spaces needed to move
            obstspaces = line.split(" ")[1]
            #append the obstpos to the global class variable
            self.obstacles[0].append(int(obstpos))
            #do the same for obstspaces
            self.obstacles[1].append(int(obstspaces))
        #the sollowing two lines are test code to make sure that the obstacles are being read properly
        #print(self.obstacles[0])
        #print(self.obstacles[1])

#create the main boardgame variable to kick this whole thing off
boardgame = game()