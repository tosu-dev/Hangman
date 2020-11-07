from os import system
from donnees import *
from fonctions import *
import os
import pickle
from pathlib import Path


if __name__ == '__main__':
	
	os.system("cls")

	# if the file does not exist
	if os.path.exists("scores") == False:
		# we create it with an empty dict
		with open("scores", "wb") as scoresFile:
			scoresPutData = pickle.Pickler(scoresFile)
			scoresPutData.dump({})
			scoresFile.close()

	# we load the file in a var
	with open("scores","rb") as scoresFile:
		scoresGetData = pickle.Unpickler(scoresFile)
		scores = scoresGetData.load()
		scoresFile.close()

	# we ask his username
	showLeaderbord(scores)
	username = askUsername()

	# if this users neverd played before
	if username not in scores.keys():
		# we register him in the dict
		scores[username] = 0

	# start
	start = False
	while not start:
		showLeaderbord(scores)
		start = input("Start ? (o/n): ")
		if start.lower() == 'o':
			start = True
		else:
			start = False
		system('cls')

	# he plays
	game()

	# we change his score if the score is better
	if scores[username] < getLives() * len(getWord()):
			lenWord = 0
			letterInWord = []
			for letter in getWord():
				if letter not in letterInWord:
					lenWord += 1

			scores[username] = getLives() * lenWord

	# we register the new score in the file
	with open("scores", "wb") as scoresFile:
		scoresPutData = pickle.Pickler(scoresFile)
		scoresPutData.dump(scores)
		scoresFile.close()

	os.system("pause")