from itertools import permutations

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        
        allGrayCodes = self.__generateGrayCodes(n)
        
        
        
        N = len(allGrayCodes)
        for i in range(N):
            allGrayCodes[i] = int( allGrayCodes[i], 2 )
        
        
        myAns = []
        startIndex = allGrayCodes.index(start)
        
        for i in range(startIndex, N):
            myAns.append( allGrayCodes[i] )
        for i in range(0, startIndex):
            myAns.append( allGrayCodes[i] )
            
        return myAns
    
    def __generateGrayCodes(self, n):
        
        if n <= 1:
            return ['0', '1']
        
        newList = []
        tempList = self.__generateGrayCodes(n-1)
        
        for elem in tempList:
            newList.append('0'+elem)
        for elem in tempList[::-1]:
            newList.append('1'+elem)
            
        return newList
    