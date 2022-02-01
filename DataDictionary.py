#Contains Character Data Class and associated functions

def initializeDataDictionary():
    #create one character data ojbect for each char a-z
    #return dictionary of data object where the keys are 0-25
    dDict= {}
    for x in range(26):
        dDict.update({x:CharacterData()})

    return dDict

def getKnownLetters(dataDictionary):
    #returns all letters that are in the word, but do not yet have defined position
    letters = []
    for x in dataDictionary.keys():
        if (dataDictionary.get(x).inWord == 1) and (dataDictionary.get(x).positionKnown == False):
            letters.append(x)
    return letters
    

def getDefinedLetter(dataDictionary, position):
    #returns the character code of a character that is known to occupy the word at the given position
    for x in dataDictionary.keys():
        if dataDictionary.get(x).positionInfo[position] == 1:
            return x



class CharacterData(object):
    """CharacterData Stores Relevant wordle info for a character, presence in the soluyion word, position, etc"""
    def __init__(self):
        # -1 is unknown, 0 is not in word, 1 is in word
        self.inWord = -1
        # -1 == could be here, 0 == not here, 1 == here
        self.positionInfo = [-1,-1,-1,-1,-1]
        # Stores a boolean for position known, to save computation later
        self.positionKnown = False