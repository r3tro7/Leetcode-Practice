def findFloor(self,A,N,X):
        #Your code here
        if(A[0] > X):
            return -1
        start = 0
        end = N - 1
        
        while(end >= start):
            mid = start + ((end - start)//2)
            
            if(X > A[mid]):
                 start = mid + 1
            elif(X < A[mid]):
                end = mid - 1
            else:
                return mid   
        return end