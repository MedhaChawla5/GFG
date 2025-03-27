class Solution:
    def rec(self,root , res):
        if root is None:
            return 0
        lh = self.rec(root.left , res)
        rh = self.rec(root.right , res)
        res[0] = max( res[0] , lh+rh)
        
        return 1+max(lh,rh)
        
    def diameter(self, root):
        # Your code here
        res = [0]
        self.rec(root , res)
        return res[0] 
