class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        left = 0 
        right = m-1
        top = 0
        bottom = n-1
        res = []
        
        while top<=bottom and left<= right:
            
            for i in range(left , right+1):
                res.append(mat[top][i])
            top = top+1
            
            for i in range(top , bottom+1):
                res.append(mat[i][right])
            right = right-1
            
            if top<=bottom:
                for i in range(right , left-1 , -1):
                    res.append(mat[bottom][i])
                bottom = bottom-1
            
            if left<=right:
                for i in range(bottom , top-1 , -1):
                    res.append(mat[i][left])
                left = left+1 
        return res
