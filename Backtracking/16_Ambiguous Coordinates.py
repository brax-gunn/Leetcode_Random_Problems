class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        allComb = []
        self.__getAllCombinations(0, len(s), s, False, False, '', allComb)
        return allComb
    
    def __isNumValid(self, num):
        if '.' in num:
            part1, part2 = num.split('.')
            if part1 != '0' and part1[0] == '0':
                return False
            else:
                return part2[-1] != '0'
        else:
            if num == '0':
                return True
            else:
                return (num[0] != '0')

    
    def __isValidComb(self, currentComb):
        if ',' in currentComb:
            x, y = currentComb[1:len(currentComb)-1].split(', ')
            return self.__isNumValid(x) and self.__isNumValid(y)
        else:
            return False
    
    def __getAllCombinations(self, currentIndex, lastIndex, myStr, commaUsed, dotUsed, currentComb, allComb):
        
        if currentIndex >= lastIndex:
            if self.__isValidComb(currentComb):
                allComb.append( currentComb )
            return
        
        # add ,
        if commaUsed is False and currentIndex > 1 and currentIndex < lastIndex-1  and currentComb[-1] != '.':
            self.__getAllCombinations(currentIndex, lastIndex, myStr, True, False, currentComb+', ', allComb) 
        
        # add .
        if dotUsed is False and  currentIndex > 1 and currentIndex < lastIndex-1 and currentComb[-1] != ' ':
            self.__getAllCombinations(currentIndex, lastIndex, myStr, commaUsed, True, currentComb+'.', allComb)
            
        # ignore both
        self.__getAllCombinations(currentIndex+1, lastIndex, myStr, commaUsed, dotUsed, currentComb+myStr[currentIndex], allComb)
        
        return
            