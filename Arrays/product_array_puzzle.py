class Solution:
    def productExceptSelf(self, arr):
        
        n = len(arr)
        pref = [1]*n
        suf = [1]*n
        res = [1]*n
        
        for i in range(1,n):
            pref[i] = arr[i-1]*pref[i-1]
        for i in range(n-2 , -1 , -1):
            suf[i] = arr[i+1]*suf[i+1]
        for i in range(n):
            res[i] = pref[i]*suf[i]
        return res
