class Solution:
    def findCatalan(self, n):
        # code here
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2 , n+1):
            dp[i]=0
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
#for valid paran : find(n/2) catalan if even n , if odd n then ans : 0
#for triangulating polygon , find (n-2) catalan's number 
