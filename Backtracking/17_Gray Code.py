class Solution:
    def grayCode(self, n: int) -> List[int]:
        allGrayCodes = self.__generateGrayCodes(n)
        N = len(allGrayCodes)
        
        for i in range(N):
            allGrayCodes[i] = int( allGrayCodes[i], 2 )
        return allGrayCodes
    
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