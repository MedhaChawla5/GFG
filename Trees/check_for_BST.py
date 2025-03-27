class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        if root is None:
            return True
        #code here
        res = []
        def helper(node):
            if node is None:
                return []
            helper(node.left)
            res.append(node.data)
            helper(node.right)
        helper(root)
        #print(res)
        if sorted(res)==res:
            return True
        else:
            return False
