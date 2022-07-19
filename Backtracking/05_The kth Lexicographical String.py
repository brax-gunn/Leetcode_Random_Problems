class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        allHappyStrings = []
        self.__generateAllHappyStrings(n, '', '#', allHappyStrings)
        # print(allHappyStrings)
        
        if k-1 >= len(allHappyStrings):
            return ''
        else:
            return allHappyStrings[k-1]
    
    def __generateAllHappyStrings(self, n, currentStr, prevChar, allHappyStrings):
        
        
        if n <= 0:
            allHappyStrings.append(currentStr)
            return
        
        for happyChar in ['a', 'b', 'c']:
            if happyChar != prevChar:
                self.__generateAllHappyStrings(n-1, currentStr+happyChar, happyChar, allHappyStrings)
        
        return
        