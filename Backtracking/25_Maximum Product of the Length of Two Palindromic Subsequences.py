from collections import defaultdict

class Solution:
    def maxProduct(self, s: str) -> int:
        
        N, pali = len(s), {}
        
        for mask in range(1, 1<<N):
            subseq = ""
            for i in range(N):
                if mask & (1<<i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)
        
        ans = 0
        
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    ans = max(ans, pali[m1]*pali[m2])
        return ans