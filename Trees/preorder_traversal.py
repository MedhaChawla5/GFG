class Solution:
#Function to return a list containing the preorder traversal of the tree.
    def preorder(self,root):
        if root is None:
            return []
        return [root.data] + self.preorder(root.left) + self.preorder(root.right)
        
   
