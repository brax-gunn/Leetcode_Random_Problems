class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        cookies = cookies[::-1]
        
        N = len(cookies)
        
        unfairness = [ float('inf') ]
        
        children = [ 0 for _ in range(k) ]
        
        self. __cookieDist( 0, N, k, children, cookies, unfairness)

        return unfairness[0]
    
    def __cookieDist(self, currentIndex, endIndex, K, children, cookies, unfairness):
        
        if currentIndex >= endIndex:
            unfairness[0] = min( unfairness[0],  max(children) )
            return
        
        if max(children) >= unfairness[0]:
            return
            
        
        for i in range(K):
            children[i]+= cookies[currentIndex]
            self.__cookieDist(currentIndex+1, endIndex, K, children, cookies, unfairness)
            children[i] -= cookies[currentIndex]

        
        return