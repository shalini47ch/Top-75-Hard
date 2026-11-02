# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        #so here we need to find the sum in a specific range 
        if not root:
            return 0
        #now lets first handle the boundaries 
        if(root.val<low):
            #means move to right
            return self.rangeSumBST(root.right,low,high)
        elif(root.val>high):
            #so move to left
            return self.rangeSumBST(root.left,low,high)
        else:
            return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
        