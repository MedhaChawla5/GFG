class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d%n
        arr[:d] = reversed(arr[:d])
        arr[d:] = reversed(arr[d:])
        arr.reverse()
