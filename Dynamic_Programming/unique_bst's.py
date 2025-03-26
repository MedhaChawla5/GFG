class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,n):
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                left = dp[j-1]
                right = dp[i-j]
                dp[i] += left*right
        return dp[n]
