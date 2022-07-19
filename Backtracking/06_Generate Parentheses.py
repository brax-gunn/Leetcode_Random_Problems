class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        allParenthesis = []
        self.__generateAllParenthesis(0, 0, n, '', allParenthesis)
        return allParenthesis
    
    
    def __generateAllParenthesis(self, openBracket, closeBracket, totalBracket, currentComb, allParenthesis):
        
        if openBracket >= totalBracket and closeBracket >= totalBracket:
            allParenthesis.append(currentComb)
            return
        
        
        # open bracket
        if openBracket < totalBracket:
            self.__generateAllParenthesis(openBracket+1, closeBracket, totalBracket, currentComb+'(', allParenthesis)
        
        # close bracket
        if openBracket > closeBracket:
            self.__generateAllParenthesis(openBracket, closeBracket+1, totalBracket, currentComb+')', allParenthesis)
            
        return