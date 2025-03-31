class Solution:
    def find(self , node , path , paths):
        if node is None:
            return 
        path.append(node.data)
        
        if node.left is None and node.right is None:
            paths.append(list(path))
        else:
            self.find(node.left , path , paths)
            self.find(node.right , path , paths)
        path.pop()
        
    def Paths(self, root):
        paths = []
        self.find(root , [] , paths)
        return paths
