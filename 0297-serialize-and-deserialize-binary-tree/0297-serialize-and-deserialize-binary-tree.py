# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #means here we need to convert to string 
        res=[]
        def dfs(node):
            if not node:
                res.append("N")
                return 
            #now do exactly as we do in preorder that is root left right 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #now here from that string we need to convert it to a given tree
        values=iter(data.split(","))
        def dfs():
            val=next(values)
            if(val=="N"):
                return None
            root=TreeNode(int(val))
            root.left=dfs()
            root.right=dfs()
            return root
        return dfs()
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))