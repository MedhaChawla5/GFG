class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [0]*(n+1)
        for i in range(n+1):
            for j in range(1 , i+1):
                dp[i] = max(dp[i] , price[j-1] + dp[i-j])
        return dp[n]
