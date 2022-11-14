class Solution: 
    def select(self, arr, i):
        # code here 
        current_min = i
        for x in range(i+1,len(arr)):
            if(arr[x] < arr[current_min]):
                current_min = x
        
        arr[i] , arr[current_min] = arr[current_min], arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            self.select(arr,i)