from os import system
import random
import os
from donnees import *

# _____FUNCTIONS_____
def randomWord(l=list()):
	"""
	choose a random word in a list of word
	:return: str
	"""
	return l[random.randint(0, len(l)-1)]

def getWord():
	"""
	get the word
	:return: str
	""" 
	return randomWord(listWords)


def game(word=getWord()):

	global lives

	while lives > 0 or hiddenWord != word:

		if lives <= maxLives:
			print(getDraw())

		# Current hints found
		hiddenWord = ""
		for i in range(len(word)):
			if word[i] in trashLetter:
				hiddenWord += word[i]
			else:
				hiddenWord += "*"
		print("{}".format(hiddenWord))


		# Check if he won or if he lost
		if lives == 0:
			os.system("cls")
			print(getDraw())
			print("You are hung, the word was \"{}\"\n".format(word))
			break
		elif hiddenWord == word:
			os.system("cls")
			print("Well played, you found the word\n")
			break


		# Else, ask a letter
		letter = ''
		while letter == '':
			letter = input("Put one letter : ").upper()
		# Check if the letter is valid
			# If no
			if len(letter) != 1 or letter not in alphabet:
				system('cls')
				print(getDraw())
				letter = ''
				continue
			# If yes	
			else:
				# If letter is in word and not already said
				if letter in word and letter not in trashLetter:
					trashLetter.append(letter)
					os.system("cls")
				# If letter is not in word and already said
				elif letter not in word and letter not in trashLetter:
					lives -= 1
					trashLetter.append(letter)
					os.system("cls")
				# If the letter is in word and already said
				elif letter in word and letter in trashLetter:
					os.system("cls")
				# If letter is not in word and already said
				elif letter not in word and letter in trashLetter:
					lives -= 1
					os.system("cls")

def getLives():
	"""
	get the amout of remaining lives
	:return: int
	"""
	return lives

def getDraw():
	"""
	get the draw string to show it
	:return: str
	"""
	return draws[maxLives - lives]

def askUsername():
	"""
	ask a username
	:return: str
	"""
	username = input("What is your username : ")
	os.system("cls")
	return username

def showLeaderbord(scores):
	print("\n[LEADERBOARD]")
	for key, value in scores.items():
		print("- {}: {}".format(key, value))
	print("\n")
