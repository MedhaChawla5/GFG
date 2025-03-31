class Solution:
    def btt(self , mp, preorder , preidx , left , right):
        if left > right:
            return None
        rootval = preorder[preidx[0]]
        root = Node(rootval)
        preidx[0] +=1
        index = mp[rootval]
        root.left = self.btt(mp , preorder , preidx , left , index-1)
        root.right = self.btt(mp , preorder , preidx , index+1 , right)
        return root
        
        
    def buildTree(self, inorder, preorder):
        mp = {value : idx for idx , value in enumerate(inorder)}
        preidx = [0]
        
        return self.btt(mp, preorder , preidx , 0 , len(inorder)-1)
