class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        swapped = False
        for i in range(n-1):
        #no need to check for last element as swap requires 2 elements 
            
            for j in range(n-i-1):
                
                if(arr[j] > arr[j+1]):
                    arr[j] , arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                    
            if(swapped == False):
                break