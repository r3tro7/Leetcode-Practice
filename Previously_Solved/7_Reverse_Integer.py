#Solution 1
class Solution:
    def reverse(self, x: int) -> int:
        #num:int = abs(x)
        negFlag:int = -1 if x<0 else 1
        final:int = 0
        x:int = abs(x)
        
        while(x):
            #rem:int = num % 10
            if(final > pow(2,31)//10):
                return 0
            final = final*10 + x%10
            x //= 10
            
            
        # if((final > pow(2, 31))) or (final <  (-abs(pow(2, 31)) - 1)):
        #as the environment doesn't allow us to store 64bit, this solution is more like a hack
        # if(final > pow(2, 31)):
        #     return 0
        
        return final*negFlag





#Solution 2
#as the environment doesn't allow us to store 64bit, this solution is more like a hack
class Solution:
    def reverse(self, x: int) -> int:
        #num:int = abs(x)
        negFlag:int = -1 if x<0 else 1
        final:int = 0
        x:int = abs(x)
        
        while(x):
            #rem:int = num % 10
            final = final*10 + x%10
            x //= 10
            
            
        # if((final > pow(2, 31))) or (final <  (-abs(pow(2, 31)) - 1)):
        #as the environment doesn't allow us to store 64bit, this solution is more like a hack
        if(final > pow(2, 31)):
            return 0
        
        return final*negFlag
        