class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        allSubsets = []
        self.__generateSubset(nums,0,len(nums),[], allSubsets)
        
        
        sumOfXor = 0
        for subset in allSubsets:
            sumOfXor += self.__calculateXOR(subset)
        return sumOfXor
    
    
    def __generateSubset(self,nums,ci,n,temp, allSubsets):
        if ci >= n:
            allSubsets.append(temp.copy())
            return
        
        
        temp.append( nums[ci] )
        self.__generateSubset(nums,ci+1,n, temp, allSubsets)
        
        temp.pop()
        self.__generateSubset(nums,ci+1,n,temp, allSubsets)
    
    def __calculateXOR(self, nums):
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor
        