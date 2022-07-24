class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        allComb = []
        candidates.sort()
        self.__generateAllComb(0, target, -1, candidates, [], allComb)
        
        return allComb
    
    def __generateAllComb(self, currentPos, target, prev, candidates, currentComb, allComb):
        
        if target == 0:
            allComb.append(currentComb.copy())
            return
        if target < 0:
            return
        
        for i in range(currentPos, len(candidates)):
            if candidates[i] == prev:
                continue
            currentComb.append(candidates[i])
            self.__generateAllComb(i+1, target-candidates[i], prev, candidates, currentComb, allComb)
            currentComb.pop()
            
            prev = candidates[i]
        