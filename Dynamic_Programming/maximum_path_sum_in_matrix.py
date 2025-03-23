class Solution:
    def maximumPath(self, mat):
        r = len(mat)
        c = len(mat[0])
        dp = [[0]*c for _ in range(r)]
        for i in range(c):
            dp[0][i] = mat[0][i]
        for i in range(1 , r):
            dp[i][0] = mat[i][0] + (max(dp[i-1][0] , dp[i-1][1]) if c>1 else dp[i-1][0])
        for i in range(1,r):
            for j in range(c):
                dp[i][j] = mat[i][j] + (max(dp[i-1][j] , dp[i-1][j-1] if j > 0 else 0 , dp[i-1][j+1]) if j+1<c else max(dp[i-1][j] , dp[i-1][j-1])) 
        return max(dp[r-1])
