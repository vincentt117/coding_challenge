# https://app.codesignal.com/challenge/j7RqxeRQ9BooqLYod

class Trie:
    def __init__(self):
        self.sufix = {}

masterTrie = Trie()

def differentSubstringsTrie(inputString):
    count = 0
    for i in range(len(inputString)):
        count += getUniques(inputString[i:])
    return count

def getUniques(inputString):
    currCount = 0
    activeTrie = masterTrie
    for i in range(len(inputString)):
        if inputString[i] not in activeTrie.sufix:
            activeTrie.sufix[inputString[i]] = Trie()
            currCount += 1
        activeTrie = activeTrie.sufix[inputString[i]]
    return currCount
    
    
    
