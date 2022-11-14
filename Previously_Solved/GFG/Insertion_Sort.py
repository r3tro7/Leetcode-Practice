class Solution:
    def insert(self, alist, index, n):
        #code here
        current = alist[index]
        position = index
        while((position > 0) and (current < alist[position-1])):
            alist[position] = alist[position-1]
            position-=1
            
        arr[position] = current
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(1,n):
            self.insert(alist,i,n)