class Solution:
    def leftRotate(self, arr, k, n):
        # Your code goes here
        start = (k % len(arr))
        # track = k%len(arr)
        temp = arr[:start]
        for i in range(n-start):
            arr[i] = arr[i+start]
            # start+=1
        arr[(n-start):] = temp