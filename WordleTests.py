#method test code for WordleBot
from WordleHelper import *

def traversalTester():
    testTrie= Trie()
    testDict= initializeDataDictionary()
    testTrie.insert('wierd')
    testTrie.insert('sweat')
    char= charToIndex('i')
    testDict.get(char).positionInfo = [-1,1,-1,-1,-1]
    testDict.get(char).inWord = 1
    testDict.get(char).positionKnown = True
    word= traverseTrie(testTrie.root,[char],0,testDict)
    print(word)


def testWordleTrie():
    file1 = open('five_letter_words.txt', 'r')
    wordleTrie = Trie()
    line = file1.readline()
    line = line[:-1]
    print(line)
    wordleTrie.insert(line)

def testDictUpdate():
    testDict= initializeDataDictionary()
    testGuess= ['w','i','e','r','d']
    testClues= [1,0,0,0,2]
    updateDictionary(testGuess,testClues,testDict)
    print(testDict.get(charToIndex('w')).inWord)
    print(testDict.get(charToIndex('w')).positionInfo)
    print(testDict.get(charToIndex('e')).positionInfo)
    print(testDict.get(charToIndex('i')).positionInfo)
    print(testDict.get(charToIndex('r')).positionInfo)
    print(testDict.get(charToIndex('d')).inWord)
    print(testDict.get(charToIndex('d')).positionKnown)
    print(testDict.get(charToIndex('d')).positionInfo)