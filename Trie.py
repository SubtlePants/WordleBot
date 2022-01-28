#Python Implementation of the Trie for WordleBot
#Assumes that all words added to Trie are the same length (5 characters with all lower case letters)

class TrieNode:
	"""The Node of the Trie"""
	def __init__(self):
		#Initialize one child for each letter to null value
		self.children = [None]*26

		#Initialize value to mark end of word to false
		self.isEndOfWord = False


class Trie:
	"""The Trie Iteslf"""
	def __init__(self):
		self.root = self.getNode()

	#returns TrieNode initialized to null
	def getNode(self):
		return TrieNode()


	def insert(self,key):
		currentLevel= self.root
		length = len(key)
		
		for l in range(length):
			index = key[l]
			if not currentLevel.children[index]:
				currentLevel.children[index] = self.getNode
			#Iterate the currentlevel
			currentLevel = currentLevel.children[index]

		#mark the last node as the leaf
		currentLevel.isEndOfWord = True


	def search(self,key):
		currentLevel= self.root
		length = len(key)

		for l in range(length):
			index = key[l]
			if not currentLevel.children[index]:
				return False
			currentLevel= currentLevel[index]

		return currentLevel.isEndOfWord