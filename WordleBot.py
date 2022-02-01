#!/usr/bin/env python

#The main file for WordleBot, start by querying the user for the initial guess and clues then suggest a word and query for clues until word is found or 6 guesses run out.

from WordleHelper import *

#initialize variables needed
currentGuess = ""
wordleTrie = buildWordleTrie()
charData = initializeDataDictionary()

#ask for first guess
currentGuess = input("Enter your first guess: ")
currentGuess = currentGuess.lower()
print(currentGuess)

#ask for first clues
currentClues = input("Enter your first clues: ")
updateDictionary(currentGuess,currentClues,charData)

#give next suggestion word suggestion
nextGuess= getNextWord(charData,wordleTrie)
print("Your next guess should be " + nextGuess)

#ask for clues and present word 3
currentGuess = nextGuess
currentClues = input("Enter the next clue: ")
updateDictionary(currentGuess,currentClues,charData)

nextGuess= getNextWord(charData,wordleTrie)
print("Your next guess should be " + nextGuess)

#ask for clues and present word 4
currentGuess = nextGuess
currentClues = input("Enter the next clue: ")
updateDictionary(currentGuess,currentClues,charData)

nextGuess= getNextWord(charData,wordleTrie)
print("Your next guess should be " + nextGuess)

#ask for clues and present word 5
currentGuess = nextGuess
currentClues = input("Enter the next clue: ")
updateDictionary(currentGuess,currentClues,charData)

nextGuess= getNextWord(charData,wordleTrie)
print("Your next guess should be " + nextGuess)

#ask for clues and present word 6
currentGuess = nextGuess
currentClues = input("Enter the next clue: ")
updateDictionary(currentGuess,currentClues,charData)

nextGuess= getNextWord(charData,wordleTrie)
print("Your next guess should be " + nextGuess)