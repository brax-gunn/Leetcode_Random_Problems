class Solution:
    def countArrangement(self, n: int) -> int:
        visitedArr = [False for _ in range(n+1)]
        self.__count = 0
        self.__calcBeauty(1, n, visitedArr)
        return self.__count
    
    def __calcBeauty(self, currentIndex, lastIndex, visitedArr):
        
        if currentIndex > lastIndex:
            self.__count += 1
            return
        
        for i in range(1,lastIndex+1):
            if (visitedArr[i] == False) and (currentIndex % i == 0 or i % currentIndex == 0):
                visitedArr[i] = True
                self.__calcBeauty(currentIndex+1, lastIndex, visitedArr)
                visitedArr[i] = False
                
        return  
        