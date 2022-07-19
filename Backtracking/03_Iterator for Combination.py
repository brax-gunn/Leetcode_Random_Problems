class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.__allCombinations = []
        self.__generateCombinations(0, characters, combinationLength, '')
        self.__currentIndex = 0
        self.__endIndex = len(self.__allCombinations)
    
    def __generateCombinations(self, currentIndex, characters, combinationLength, currentCombination):
            
        if combinationLength <= 0:
            self.__allCombinations.append(currentCombination)
            return
        
        if currentIndex >= len(characters):
            return
        
        # include elem
        self.__generateCombinations(currentIndex+1, characters, combinationLength-1, currentCombination+characters[currentIndex])
        
        # exclude elem
        self.__generateCombinations(currentIndex+1, characters, combinationLength, currentCombination)
        return
        
        

    def next(self) -> str:
        nextComb = self.__allCombinations[self.__currentIndex]
        self.__currentIndex += 1
        return nextComb
        

    def hasNext(self) -> bool:
        if self.__currentIndex < self.__endIndex:
            return True
        else:
            return False
        