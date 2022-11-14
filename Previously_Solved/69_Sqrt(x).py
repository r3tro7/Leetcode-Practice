class Solution:
    def mySqrt(self, x: int) -> int:
        
        if(x == 0 or x == 1):
            return x
        start = 1
        end = x // 2
        
        while(end >= start):
            mid = start + ((end - start)//2)
            
            if(mid < (x/mid)):
                start = mid + 1
            elif(mid > (x/mid)):
                end = mid - 1
            else:
                return mid
        return end
            
        