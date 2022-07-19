class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        charFrq = {} 
        for char in tiles:
            if char not in charFrq:
                charFrq[char] = 1
            else:
                charFrq[char] += 1

        return self.__calcAllComb(charFrq)
                
    
    def __calcAllComb(self, charFrq):
        
        if sum(charFrq.values()) <= 0:
            return 0
        
        ans = 0
        for char in charFrq.keys():
            if charFrq[char] > 0:
                charFrq[char] -= 1
                ans += self.__calcAllComb(charFrq) + 1
                charFrq[char] += 1
        
        return ans
                    
        