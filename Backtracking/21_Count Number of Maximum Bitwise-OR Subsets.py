from collections import defaultdict

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        self.__generateAllSubset(0, len(nums), nums, 0, memo)
        return memo[ max(memo) ]
    
    def __generateAllSubset(self, currentIndex, lastIndex, nums, currentOr, memo):
        
        if currentIndex >= lastIndex:
            memo[currentOr] += 1
            return
        
        # include current elem
        self.__generateAllSubset(currentIndex+1, lastIndex, nums, currentOr | nums[currentIndex], memo)
        
        # exclude current elem
        self.__generateAllSubset(currentIndex+1, lastIndex, nums, currentOr, memo)
        
        return