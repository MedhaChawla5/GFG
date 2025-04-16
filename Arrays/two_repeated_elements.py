class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, n, arr):
        freq = [0]*n
        res = []
        
        for i in arr:
            freq[i-1]+=1
            if freq[i-1]==2:
                res.append(i)
        return res 
