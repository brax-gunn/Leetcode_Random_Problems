class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        allPath = []
        
        startRow = -1
        startCol = -1
        endRow = -1
        endCol = -1
        
        totalNonBlocks = 0
        
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                if grid[i][j] == 1:
                    startRow = i
                    startCol = j
                elif grid[i][j] == 2:
                    endRow = i
                    endCol = j
                elif grid[i][j] == 0:
                    totalNonBlocks += 1
                    
        # print(startRow, startCol, endRow, endCol)
        self.__moveRobot(startRow, startCol, endRow, endCol, grid, [], allPath, {}, totalNonBlocks)
        
        return len(allPath)
    
    def __moveRobot(self, currentRow, currentCol, endRow, endCol, grid, currentPath, allPath, visitedArr, totalNonBlocks):
        
        if currentRow == endRow and currentCol == endCol:
            currentPath.append( (currentRow, currentCol) )
            if len(currentPath) == totalNonBlocks + 2:
                allPath.append( currentPath.copy() )
            currentPath.pop()
            return
        
        if currentRow < 0 or currentRow >= len(grid) or currentCol < 0 or currentCol >= len(grid[0]):
            return
        
        if grid[currentRow][currentCol] == -1:
            return
        
        if (currentRow, currentCol) in visitedArr:
            return
        
        visitedArr[(currentRow, currentCol)] = True
        currentPath.append( (currentRow, currentCol) )
        
        # move right
        self.__moveRobot(currentRow, currentCol+1, endRow, endCol, grid, currentPath, allPath, visitedArr, totalNonBlocks)
        
        # move down
        self.__moveRobot(currentRow+1, currentCol, endRow, endCol, grid, currentPath, allPath, visitedArr, totalNonBlocks)
        
        # move left
        self.__moveRobot(currentRow, currentCol-1, endRow, endCol, grid, currentPath, allPath, visitedArr, totalNonBlocks)
        
        # move up
        self.__moveRobot(currentRow-1, currentCol, endRow, endCol, grid, currentPath, allPath, visitedArr, totalNonBlocks)
        
        currentPath.pop()
        del visitedArr[(currentRow, currentCol)]
        
        return