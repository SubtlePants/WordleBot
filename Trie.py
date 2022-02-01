#Python Implementation of the Trie for WordleBot
#Assumes that all words added to Trie are the same length (5 characters with all lower case letters)

def charToIndex(chr):
        #returns a lowercase character encoded as an integer with 'a' == 0 and 'z' == 25
        return ord(chr) - ord('a')
def indexToChar(ind):
        #returns a lowercase character from it's encoding as an integer
        return chr(ind + ord('a'))

class TrieNode:
        """The Node of the Trie"""
        def __init__(self):
                #Initialize one child for each letter to null value
                self.children = [None]*26

                #Initialize value to mark end of word to false
                self.isEndOfWord = False

        def whatAmI(self):
                print("I am a TrieNode")
                pass


class Trie:
        """The Trie Iteslf"""
        def __init__(self):
                self.root = self.getNode()

        #returns TrieNode initialized to null
        def getNode(self):
                return TrieNode()

        def insert(self,key):
                pCrawl = self.root
                length = len(key)
                for l in range(length):
                        index = key[l]
                        index = charToIndex(index)
                        #print(index)
                        if not pCrawl.children[index]:
                                pCrawl.children[index] = self.getNode()
                        #Iterate the pCrawl
                        pCrawl = pCrawl.children[index]

                #mark the last node as the leaf
                pCrawl.isEndOfWord = True

        def search(self,key):
                pCrawl = self.root
                length = len(key)

                for l in range(length):
                        index = key[l]
                        index = charToIndex(index)
                        #print(index)
                        if not pCrawl.children[index]:
                                return False
                        pCrawl= pCrawl.children[index]

                return pCrawl.isEndOfWord
