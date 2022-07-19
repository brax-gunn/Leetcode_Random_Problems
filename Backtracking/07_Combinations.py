class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allComb = []
        self.__generateAllCombination([], allComb, k, n, 0)
        # print(allComb)
        return allComb
    
    def __generateAllCombination(self, currentComb, allComb, k, n, prevElem):
        
        if k <= 0:
            allComb.append(currentComb.copy())
            return
            
        
        for elem in range(prevElem+1,n+1):
            currentComb.append(elem)
            self.__generateAllCombination(currentComb, allComb, k-1, n, elem)
            currentComb.pop()
        
        return