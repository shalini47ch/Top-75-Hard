# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #0 means uncovered,1 means has camera and 2 means covered
        self.cameras=0
        def dfs(node):
            if not node:
                return 2
            #recursively do for left and right
            left=dfs(node.left)
            right=dfs(node.right)
            if(left==0 or right==0):
                self.cameras+=1
                return 1
            if(left==1 or right==1):
                return 2
            return 0
        #now here we call dfs if it gives uncovered then we increase the no of cameras
        if(dfs(root)==0):
            self.cameras+=1
        return self.cameras
       