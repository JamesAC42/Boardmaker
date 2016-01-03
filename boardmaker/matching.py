from boardmaker import *
from random import shuffle
from time import sleep
from itertools import chain

def game():
	board_display = makeBoard(4,4)

	values = list("ABCDEFGH") * 2
	shuffle(values)
	values = [values[x:x+4] for x in range(0, len(values), 4)]

	stop = False
	
	def guess():
		one = [1,2,3,4]
		two = [5,6,7,8]
		three = [9,10,11,12]
		four = [13,14,15,16]
		coordinates = []
		
		while True:
			spot = input("Guess: ")
			try:
				spot = int(spot)
				if spot not in range(1,17):
					print("Invalid. Input a number 1-16.")
					continue
				break
			except ValueError:
				print("Invalid. Input a number 1-16.")
				continue
				
		if spot < 5:
			coordinates.append(0)
			for i in range(0,4):
				if spot == one[i]:
					coordinates.append(i)
		elif spot < 9:
			coordinates.append(1)
			for i in range(0,4):
				if spot == two[i]:
					coordinates.append(i)
		elif spot < 13:
			coordinates.append(2)
			for i in range(0,4):
				if spot == three[i]:
					coordinates.append(i)
		else:
			coordinates.append(3)
			for i in range(0,4):
				if spot == four[i]:
					coordinates.append(i)
		return coordinates

	while True:
		board_display.printBoard()
		while True:
			guess1 = guess()
			if board_display.getIndex(guess1) != " ":
				print("Space already matched.")
				continue
			else:
				break
		guess1_value = values[guess1[0]][guess1[1]]
		board_display.changeIndex(guess1, guess1_value)
		board_display.printBoard()
		
		while True:
			guess2 = guess()
			if guess2 == guess1:
				print("Invalid. You already guessed that.")
				continue
			elif board_display.getIndex(guess2) != " ":
				print("Space already matched.")
				continue
			else:
				break
		guess2_value = values[guess2[0]][guess2[1]]	
		board_display.changeIndex(guess2,guess2_value)
		board_display.printBoard()
		
		sleep(1)
		
		if guess1_value == guess2_value:
			print("MATCH!")
			x = 0
			display_values = board_display.getList()
			for i in chain(display_values):
				if i != " ":
					x = x + 1
			if x == 16:
				print("You Win!")
				while True:
					replay = input("Again? (y/n):")
					if replay.lower() == "y":
						game()
						break
					elif replay.lower() == "n":
						stop = True
						break
					else:
						print("Invalid response")
		else:
			print("NO MATCH")
			board_display.changeIndex(guess1, " ")
			board_display.changeIndex(guess2, " ")
		if stop == True:
			break
	
game()	
	
	
	
	
	
	
	