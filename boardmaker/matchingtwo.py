#!/usr/bin/py

from boardmaker import *
from random import shuffle
from time import sleep

class MatchingGame:
    def __init__(self):
        self.start()
    def spaceHelp(self):
        self.helpBoard.printBoard()
        input("Press enter to continue: ")
        self.board_display.printBoard()
    def getGuessCoordinates(self):
        tLength = self.tLength
        coordinates = []
        spotHelp = self.spotHelp
        while True:
            try:
                spot = input("Guess: ")
                if spot == "help":
                    self.spaceHelp()
                    continue
                else:
                    spot = int(spot)
                    if spot not in range(1,tLength+1):
                        print("Invalid. Input a number 1-{}.".format(tLength))
                        continue
                break
            except ValueError:
                print("Invalid. Input a number 1-{}.".format(tLength))
                continue
        for row in spotHelp:
            if spot in row:
                coordinates.append(spotHelp.index(row))
                coordinates.append(row.index(spot))
        return coordinates
    def guess(self):
        while True:
            guess1 = self.getGuessCoordinates()
            self.guess1 = guess1
            if self.board_display.getIndex(guess1) != " ":
                print("Space already matched. ")
                continue
            else:
                break
        guess1_value = self.values[guess1[0]][guess1[1]]
        self.board_display.changeIndex(guess1, guess1_value)
        self.board_display.printBoard()

        while True:
            guess2 = self.getGuessCoordinates()
            self.guess2 = guess2
            if guess1 == guess2:
                print("You already guessed that. Try again.")
                continue
            elif self.board_display.getIndex(guess2) != " ":
                print("Space already matched")
                continue
            else:
                break
        guess2_value = self.values[guess2[0]][guess2[1]]
        self.board_display.changeIndex(guess2, guess2_value)
        self.board_display.printBoard()

        sleep(1)

        return guess1_value == guess2_value

    def game(self):
        tLength = self.tLength
        size = self.size

        while True:
            self.board_display.printBoard()
            if self.guess():
                print("Match!")
                if not self.board_display.inBoard(" "):
                    print("You Win!")
                    self.start()
            else:
                print("No match!")
                self.board_display.changeIndex(self.guess1, " ")
                self.board_display.changeIndex(self.guess2, " ")

    def start(self):
        validSizes = [4,6,8,10]
        while True:
            try:
                size = int(input("Size (4,6,8,10): "))
                if size not in validSizes:
                    print("Valid sizes are 4, 6, 8, or 10: ")
                    continue
                else:
                    break
            except ValueError:
                print("Error. Enter Valid number.")
                continue
        print('\nTip: Type help while guessing to get space numbers\n')
        sleep(3)
        self.size = size
        self.tLength = size ** 2
        self.board_display = makeBoard(size, size)
        self.board_display.fillBoard(" ")
        temp = list(range(1, self.tLength + 1))
        self.spotHelp = [temp[x:x + self.size] for x in range(0, len(temp), self.size)]
        self.helpBoard = toBoard(self.spotHelp)
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()=+?><"
        usedChars = int(self.tLength / 2)
        values = list(characters[0:usedChars]) * 2
        shuffle(values)
        self.values = [values[x:x + size] for x in range(0, len(values), size)]
        self.game()

MatchingGame()

