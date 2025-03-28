class Solution:
    def bToDLL(self,root):
        if root is None:
            return None
        self.head = None
        self.tail = None
        
        def helper(node ):
            if node is None:
                return None
            helper(node.left)
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.right = node
                node.left = self.tail
                self.tail = node
            helper(node.right)
        helper(root)
        return self.head
