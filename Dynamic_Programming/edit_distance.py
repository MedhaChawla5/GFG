class Solution:
	def editDistance(self, s1, s2):
	    m = len(s1)
	    n = len(s2)
	    if(m==0):
	        return n 
	    if(n==0):
	        return m 
	    dp = [[0]*(n+1) for _ in range(m+1)]
	    for i in range(m+1):
	        dp[i][0] = i
	    for i in range(n+1):
	        dp[0][i] = i
	    for i in range(1,m+1):
	        for j in range(1 , n+1):
	            if (s1[i-1]!=s2[j-1]):
	                dp[i][j] = 1 + min(dp[i][j-1] , dp[i-1][j-1] , dp[i-1][j])
	            else:
	                dp[i][j] = dp[i-1][j-1]
	    return dp[m][n]
