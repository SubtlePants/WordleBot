#contains helper functions and classes for wordlebot

from Trie import *
from DataDictionary import *

def buildWordleTrie():
    #read all lines from five_letter_words.txt
    #add each word into a single Trie structure
    file1= open('five_letter_words.txt', 'r')
    wordleTrie= Trie()
    while True:
        line = file1.readline()
        #remove the line break character
        #had to add this twice when calling from outside python environment for some reason
        line = line[:-1]
        line = line[:-1]

        if not line:
            break

        wordleTrie.insert(line)

    return wordleTrie


def getNextWord(dataDict, wordleTrie):
    #assumes a data dictionary that has been updated with new information from the previous guess
    #recursively traverses the tree (DFS) to find the first elegible word based on the data dictionary
    knownLetters = getKnownLetters(dataDict)
    currentNode = wordleTrie.root
    nextWordIndexes= traverseTrie(currentNode,knownLetters,0,dataDict)
    #convert the arrray of indices to a string of characters
    nextWord = ""
    for x in nextWordIndexes:
        char= indexToChar(x)
        nextWord += char
    return nextWord
    

def traverseTrie(currentNode,letters,currentIndex,dataDict):
    #returns the remaining list of characters in a recursive call
    #currentNode is the current position on the Trie
    #letters are the remaining letter that MUST be included in the word
    #currentIndex is the spot in the word for which we are choosing a character 0-4
    #dataDict is the dictionary containing known word information

    if letters == None:
        letters = []
    
    if (len(letters) > (5 - currentIndex)):
        #BASE: it is no longer possible to fit all of the required characters so end the call
        return []

    if currentNode.isEndOfWord:
        #BASE: the word has been constructed, so end the call
        return []

    #if the next spot is known in the data dictionary, choose it if available and recurse
    #if it is known, but the letter is not available, we cannot make a word so return
    definedLetter = getDefinedLetter(dataDict, currentIndex)
    if (definedLetter != None) and (currentNode.children[definedLetter] == None):
        return []

    if (definedLetter != None) and (currentNode.children[definedLetter] != None):
        currentNode = currentNode.children[definedLetter]
        currentIndex += 1
        returnWord= [definedLetter]
        returnWord.extend(traverseTrie(currentNode,letters,currentIndex,dataDict))
        return returnWord

    #if the next node can be one of the remaining letters, traverse to that node next
    #make sure the letter chosen is available from this space in the word from the dictionary
    for char in letters:
        if currentNode.children[char] and (dataDict.get(char).positionInfo[currentIndex]!=0):
            currentNode = currentNode.children[char]
            currentIndex += 1
            letters= letters.remove(char)
            returnWord=[char]
            returnWord.extend(traverseTrie(currentNode,letters,currentIndex,dataDict))
            return returnWord

    #otherwise, find the first node that exists traverse the Trie
    #make sure the letter chosen has not yet been eliminated from the word
    for char in range(26):
        if currentNode.children[char] and (dataDict.get(char).inWord != False):
            currentNode= currentNode.children[char]
            currentIndex += 1
            returnWord=[char]
            returnWord.extend(traverseTrie(currentNode, letters, currentIndex, dataDict))
            return returnWord

    #else, no letter is available, return none
    return []

def updateDictionary(guess, clues, dataDict):
    #based on the last guess (a five letter word) and the info from wordle, update the dictionary
    #guess should be a list of characters representing the 5 letter word
    #dataDict is the dictionary storing character data
    #clues should be an array of integers with order corresponding to the letters in guess
    #0 == not in word
    #1 == in word, but wrong place
    #2 == in word, correct place

    for x in range(5):
        char = charToIndex(guess[x])

        if clues[x] == 0:
            dataDict.get(char).inWord= 0
        if clues[x] == 1:
            dataDict.get(char).inWord= 1
            dataDict.get(char).positionInfo[x] = 0
        if clues[x] == 2:
            dataDict.get(char).inWord= 1
            dataDict.get(char).positionKnown= True
            dataDict.get(char).positionInfo[x]= 1
