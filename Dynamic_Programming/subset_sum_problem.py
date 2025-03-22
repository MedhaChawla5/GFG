class Solution:
    def isSubsetSum (self, arr, sum):
        # code here
        dp = [0]*(sum+1)
        dp[0] = 1
        for x in arr:
            for i in range(sum , x-1 , -1):
                dp[i] += dp[i-x]
        #print(dp)
        if(dp[sum]):
            return True 
        else:
            return False 
        
