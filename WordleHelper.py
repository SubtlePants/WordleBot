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
        line = line[:-1]

        if not line:
            break

        wordleTrie.insert(line)

    return wordleTrie


def testWordleTrie():
    file1 = open('five_letter_words.txt', 'r')
    wordleTrie = Trie()
    line = file1.readline()
    line = line[:-1]
    print(line)
    wordleTrie.insert(line)


def getNextWord(dataDict, wordleTrie):
    #assumes a data dictionary that has been updated with new information from the previous guess
    #recursively traverses the tree (DFS) to find the first elegible word based on the data dictionary
    nextWord = []
    knownLetters = getKnownLetters(dataDict)
    currentNode = wordleTrie.root
    

def traverseTrie(currentNode,letters,currentIndex,dataDict):
    #returns the remaining list of characters in a recursive call
    #currentNode is the current position on the Trie
    #letters are the remaining letter that MUST be included in the word
    #currentIndex is the spot in the word for which we are choosing a character 0-4
    #dataDict is the dictionary containing known word information
    
    if (len(letters) > (5 - currentIndex)):
        #BASE: it is no longer possible to fit all of the required characters so end the call
        return None

    if currentNode.isEndOfWord:
        #BASE: the word has been constructed, so end the call
        return None


    #if the next spot is known in the data dictionary, choose it if available an recurse
    #if it is known, but the letter is not available, we cannot make a word so return
    definedLetter = getDefinedLetter(dataDict, currentIndex)
    if (definedLetter != None) and (currentNode.children[definedLetter] == None):
        return None

    if (definedLetter != None) and (currentNode.children[definedLetter] != None):
        currentNode = currentNode.children[definedLetter]
        currentIndex +=
        return [definedLetter].extend(traverseTrie(currentNode,letters,currentIndex,dataDict))

    