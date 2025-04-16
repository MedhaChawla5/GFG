class Solution:
    def sumClosest(self, arr, target):
        res = 0
        n = len(arr)
        arr.sort()
        mind = float('inf')
        
        for i in range(n-1):
            l = i 
            r = n-1
            while(l<r):
                currsum = arr[l]+arr[r]
                if abs(target-currsum)<mind:
                    mind = abs(target-currsum)
                    res = [arr[l],arr[r]]
                elif abs(target-currsum)==mind:
                    if (abs(res[0]-res[1])<abs(arr[l]-arr[r])):
                        res= [arr[l],arr[r]]
                if currsum < target :
                    l+=1
                else:
                    r-=1
            return res 
