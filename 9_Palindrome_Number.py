class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        
        x = str(x)
        
        for position in range(len(x)//2):
            if(x[position] != x[len(x) - position - 1]):
            # ~ is Bitwise NOT
            # if(x[position] != x[~position]):
                return False
        
#         start:int = 0
#         end:int = len(x) - 1
            
#         while(end >= start):
#             if(x[start] == x[end]):
#                 start += 1
#                 end -= 1
#             else:
#                 return False
        return True