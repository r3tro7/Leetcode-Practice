class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start:int = 0
        # end:int = (matrix.shape[0]*matrix.shape[1]) - 1
        if(len(matrix) == 0):
            return False
        
        row , col = len(matrix) , len(matrix[0])
        end:int = row*col - 1
        
        while(start<=end):
            
            mid:int = start + ((end - start)//2)
            
            if(matrix[mid//col][mid%col] > target):
                end = mid - 1
            elif(matrix[mid//col][mid%col] < target):
                start = mid + 1
            else:
                return True
        return False