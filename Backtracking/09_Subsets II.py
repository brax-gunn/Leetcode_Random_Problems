class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        allComb = []
        self.__generateAllSubsets(0, N, nums, [], allComb)
        return allComb
    
    def __generateAllSubsets(self, currentIndex, lastIndex, nums, currentComb, allComb):
        
        if currentIndex >= lastIndex:
            if currentComb not in allComb:
                allComb.append(currentComb.copy())
            return
        
        currentComb.append(nums[currentIndex])
        # include elem
        self.__generateAllSubsets(currentIndex+1, lastIndex, nums, currentComb, allComb)
        
        currentComb.pop()
        # exclude elem
        self.__generateAllSubsets(currentIndex+1, lastIndex, nums, currentComb, allComb)
        return

        