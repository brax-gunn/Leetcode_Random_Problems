class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        allPermutations = []
        self.__generateAllPermutations(0, len(s), s, '', allPermutations)
        return allPermutations
    
    def __generateAllPermutations(self, currentIndex, endIndex, givenStr, currentStr, allPermutations):
        
        if currentIndex >= endIndex:
            allPermutations.append(currentStr)
            return
        
        currentChar = givenStr[currentIndex]
        # check if number
        if ord(currentChar) >= 48 and ord(currentChar) <= 57:
            self.__generateAllPermutations(currentIndex+1, endIndex, givenStr, currentStr+givenStr[currentIndex], allPermutations)
            return
            
        # include lowercase char
        self.__generateAllPermutations(currentIndex+1, endIndex, givenStr, currentStr+givenStr[currentIndex].lower(), allPermutations)
        
        # include uppercase char
        self.__generateAllPermutations(currentIndex+1, endIndex, givenStr, currentStr+givenStr[currentIndex].upper(), allPermutations)
        
        return
        
        
        