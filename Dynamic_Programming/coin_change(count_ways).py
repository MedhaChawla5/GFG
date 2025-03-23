class Solution:
    def count(self, coins, sum):
        dp = [0]*(sum+1)
        dp[0] = 1
        for i in coins:
            for j in range(i , sum+1):
                dp[j] += dp[j-i]
        return dp[sum]
