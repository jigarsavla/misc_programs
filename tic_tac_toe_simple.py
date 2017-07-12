#!/usr/local/bin/python3

# Building Tic-Tac-Toe using Py3. 
# will be using classes

import os
os.system("clear")

class Board(object):

	def __init__(self):
		self.cells = [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

	def display(self):
		print ("%s | %s | %s" %(self.cells[1], self.cells[2], self.cells[3]))
		print ("----------")
		print ("%s | %s | %s" %(self.cells[4], self.cells[5], self.cells[6]))
		print ("----------")
		print ("%s | %s | %s" %(self.cells[7], self.cells[8], self.cells[9]))

	def update(self, cell_choice, player):
		# player can be X or O
		if (self.cells[cell_choice] == " "):
			self.cells[cell_choice] = player
			refresh_screen(self)
		else:
			print("ERR, trying to over-ride an already used location ")


def print_header():
	print ("Welcome to simple tic-tac-toe")

def refresh_screen(board):
	#clear the screen
	os.system("clear")

	# print header
	print_header()

	#show the board
	board.display()



board = Board()

#board.display()
while True:
	refresh_screen(board)

	# Get X input

	x_choice = int(input("\nX) Please choose X position 1-9 : "))

	board.update(x_choice, 'X')

	o_choice = int(input("\nO) Please choose O position 1-9 : "))

	board.update(o_choice, 'O')