class Solution:
    def kthLargest(self,root, k):
        count = 0
        res = []
        def helper(node):
            if node is None:
                return 
            helper(node.left)
            res.append(node.data)
            helper(node.right)
        helper(root)
        x = len(res)-k
        return res[x]
