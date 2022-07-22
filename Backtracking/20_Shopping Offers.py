class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        minAmount = [float('inf')]
        self.__goShopping(needs, len(needs), price, special, 0, minAmount)
        return minAmount[0]
    
    def __goShopping(self, currentNeed, N, price, special, currentAmount, minAmount):
        
        if self.__isNeedSatisfied(currentNeed):
            #print(currentAmount)
            minAmount[0] = min( minAmount[0], currentAmount )
            return
        
        if self.__isNeedNegative(currentNeed):
            return
        
        # use offer
        for offer in special:
            self.__applyOffer(currentNeed, offer, N)
            self.__goShopping(currentNeed, N, price, special, currentAmount+offer[N], minAmount)
            self.__nullifyOffer(currentNeed, offer, N)
        
        # use no offer
        defaultCost = self.__calcDefaultPrice(currentNeed, price, N)
        # self.__applyDefaultPrice(currentNeed, price, N)
        self.__goShopping([0], N, price, special, currentAmount+defaultCost, minAmount)

        return
    
    def __applyOffer(self, currentNeed, offer, N):
        
        for i in range(N):
            currentNeed[i] = currentNeed[i] - offer[i]
        
    
    def __nullifyOffer(self, currentNeed, offer, N):
        
        for i in range(N):
            currentNeed[i] = currentNeed[i] + offer[i]
        
    
    def __applyDefaultPrice(self, currentNeed, prices, N):
        
        for i in range(N):
            currentNeed[i] = 0
            
    
    def __calcDefaultPrice(self, currentNeed, prices, N):
        bill = 0
        for i in range(N):
            bill += currentNeed[i]*prices[i]
        return bill
    
    def __isNeedSatisfied(self, currentNeed):
        for elem in currentNeed:
            if elem != 0:
                return False
        return True
    
    def __isNeedNegative(self, currentNeed):
        for elem in currentNeed:
            if elem < 0:
                return True
        return False