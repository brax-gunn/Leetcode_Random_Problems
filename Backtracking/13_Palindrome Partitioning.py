class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        allSubstr = []
        self.__generatePalSubstr(0, N, s, [], allSubstr)
        return allSubstr
    
    
    def __generatePalSubstr(self, currentIndex, N, givenStr, currentSubstr, allSubstr):
        
        if currentIndex >= N:
            allSubstr.append( currentSubstr.copy() )
            return
        
        for i in range(currentIndex, N):
            if self.__isPalindrome( givenStr[currentIndex:i+1]):
                currentSubstr.append(givenStr[currentIndex:i+1])
                self.__generatePalSubstr(i+1, N, givenStr, currentSubstr, allSubstr)
                currentSubstr.pop()
        return
    
    
    
    def __isPalindrome(self, myStr):
        startIndex = 0
        endIndex = len(myStr)-1
        
        while startIndex <= endIndex:
            if myStr[startIndex] != myStr[endIndex]:
                return False
            startIndex += 1
            endIndex -= 1
        
        return True