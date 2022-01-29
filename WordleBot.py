from Trie import *

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