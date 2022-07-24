class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPerm = []
        self.__generateAllPermutation(0, len(nums), nums, [], allPerm)
        return allPerm
    
    def __generateAllPermutation(self, currentIndex, lastIndex, nums, currentPerm, allPerm):
        
        if currentIndex >= lastIndex:
            allPerm.append(currentPerm.copy())
            return
        
        for elem in nums:
            if elem in currentPerm:
                continue

            currentPerm.append( elem )
            self.__generateAllPermutation(currentIndex+1, lastIndex, nums, currentPerm, allPerm)
            currentPerm.pop()

        
        return