class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        if root is None:
            return []
        return self.postOrder(root.left) + self.postOrder(root.right) + [root.data]


