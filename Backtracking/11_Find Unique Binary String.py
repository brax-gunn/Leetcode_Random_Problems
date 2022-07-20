class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        allComb = []
        self.__generateAllComb(len(nums), '', allComb, nums)
        return allComb[0]
    
    def __generateAllComb(self, elemLeft, currentComb, allComb, nums):
        
        if elemLeft <= 0:
            if currentComb not in nums:
                allComb.append(currentComb)
                return True
            return False
            
        # include 0
        if self.__generateAllComb(elemLeft-1, currentComb+'0', allComb, nums):
            return True
        
        # include 1
        if self.__generateAllComb(elemLeft-1, currentComb+'1', allComb, nums):
            return True
        
        return False
        