# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPath = []
        if root is None:
            return []
        self.__dfs(root, 0, targetSum, [], allPath)
        return allPath
    
    def __dfs(self, root, currentSum, targetSum, currentPath, allPath):
        
        if root.left is None and root.right is None:
            currentSum += root.val
            currentPath.append(root.val)
            if currentSum == targetSum:
                print(currentPath)
                allPath.append(currentPath.copy())
            currentPath.pop()
            return
        
        currentPath.append(root.val)
        if root.left is not None:
            self.__dfs(root.left, currentSum + root.val, targetSum, currentPath, allPath)
        if root.right is not None:
            self.__dfs(root.right, currentSum + root.val, targetSum, currentPath, allPath)
        currentPath.pop()
        
        return