class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        self.__maxGold = 0
        visitedArr = {}
        for i in range(M):
            for j in range(N):
                self.__startCollectingGold(i, j, M, N, grid, 0, 0,  visitedArr)
        
        return self.__maxGold
    
    def __startCollectingGold(self, currentRow, currentCol, M, N, grid, currentGold, maxGold, visitedArr):
        
        self.__maxGold = max(self.__maxGold, currentGold)
        
        if currentRow < 0 or currentRow >= M or currentCol < 0 or currentCol >= N:
            return
        
        if grid[currentRow][currentCol] == 0:
            return
        
        if (currentRow, currentCol) in visitedArr:
            return
        
        visitedArr[ (currentRow, currentCol) ] = True
        
        # move up
        self.__startCollectingGold(currentRow-1, currentCol, M, N, grid, currentGold+grid[currentRow][currentCol], maxGold, visitedArr)
        
        # move right
        self.__startCollectingGold(currentRow, currentCol+1, M, N, grid, currentGold+grid[currentRow][currentCol], maxGold, visitedArr)
        
        # move down
        self.__startCollectingGold(currentRow+1, currentCol, M, N, grid, currentGold+grid[currentRow][currentCol], maxGold, visitedArr)
        
        # move left
        self.__startCollectingGold(currentRow, currentCol-1, M, N, grid, currentGold+grid[currentRow][currentCol], maxGold, visitedArr)
        
        del visitedArr[ (currentRow, currentCol) ]
        
        return
        