class Solution:
    def leftcollect(self, root, res):
        node = root.left
        while node:
            if not self.is_leaf(node):
                res.append(node.data)
            node = node.left if node.left else node.right  
    
    def rightcollect(self, root, res):
        node = root.right
        temp = []
        while node:
            if not self.is_leaf(node):
                temp.append(node.data)
            node = node.right if node.right else node.left  
        res.extend(temp[::-1])  
    
    def is_leaf(self, node):
        return node.left is None and node.right is None
    
    def leafcollect(self, root, res):
        if root is None:
            return
        if self.is_leaf(root):
            res.append(root.data)
        self.leafcollect(root.left, res)
        self.leafcollect(root.right, res)
    
    def boundaryTraversal(self, root):
        if root is None:
            return []
        
        res = []
        if not self.is_leaf(root):
            res.append(root.data)
        self.leftcollect(root, res)
        self.leafcollect(root, res)
        self.rightcollect(root, res)
        
        return res
