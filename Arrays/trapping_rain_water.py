class Solution:
    def maxWater(self, arr):
        n = len(arr)
        lmax = arr[0]
        rmax = arr[n-1]
        left = 1
        right = n-2
        sum = 0
        while(left<=right):
            if lmax<rmax:
                if arr[left]<lmax:
                    sum += lmax-arr[left]
                else:
                    lmax = arr[left]
                left = left +1
            else:
                if arr[right]<rmax:
                    sum += rmax-arr[right]
                else:
                    rmax = arr[right]
                right = right -1
        return sum 
