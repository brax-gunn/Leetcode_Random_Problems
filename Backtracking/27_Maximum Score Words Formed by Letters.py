from collections import defaultdict

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        memoCharCount = defaultdict(int)
        for char in letters:
            memoCharCount[char] += 1
            
        memoWordScore = defaultdict(int)
        for word in words:
            wordScore = 0
            for char in word:
                wordScore += score[ ord(char)-97 ]
            memoWordScore[word] = wordScore
                
        
        allComb = []
        maxScore = [0]
        self.__generateWordSeq(0, len(words), words, [], allComb, memoCharCount, memoWordScore, 0, maxScore)
        # print(allComb)
        return maxScore[0]
        
    def __generateWordSeq(self, currentIndex, lastIndex, words, currentComb, allComb, memoCharCount, memoWordScore, currentScore, maxScore):
        
        if currentIndex >= lastIndex:
            maxScore[0] = max( maxScore[0], currentScore )
            allComb.append( currentComb.copy() )
            return
        
        self.__generateWordSeq(currentIndex+1, lastIndex, words, currentComb, allComb, memoCharCount, memoWordScore, currentScore, maxScore)
        
        
        if self.__isValid(words[currentIndex], memoCharCount):
        
            for char in words[currentIndex]:
                memoCharCount[char] -= 1

            currentComb.append( words[currentIndex] )
            self.__generateWordSeq(currentIndex+1, lastIndex, words, currentComb, allComb, memoCharCount, memoWordScore, currentScore+memoWordScore[words[currentIndex] ], maxScore)
            currentComb.pop()

            for char in words[currentIndex]:
                memoCharCount[char] += 1
        
        return
    
    def __isValid(self, currentWord, memoCharCount):
        
        ans = True
        
        for char in currentWord:
            memoCharCount[char] -= 1
            if memoCharCount[char] < 0:
                ans = False
        
        for char in currentWord:
            memoCharCount[char] += 1
            
        return ans
        
        