class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # iterative code 1
        # low_str = (''.join(element for element in s if element.isalnum())).lower()
        # low_str_len = len(low_str)
        
        # for i in range(low_str_len//2):
        #     if(low_str[i] != low_str[low_str_len - i - 1]):
        #         return False
        # return True

        #iterative code 2
        begin, end = 0 , len(s) -1
    
        while(begin < end):
            while not s[begin].isalnum() and begin<end:
                begin+=1
            while not s[end].isalnum() and begin<end:
                end -= 1
            if(s[begin].lower() != s[end].lower()):
                return False
            else:
                begin , end = begin + 1, end - 1
        return True



# recursive code
        # return self.checkReverse(low_str)
#     def checkReverse(self,low_str,pointer=0) -> bool:
#         if(pointer >= len(low_str)//2):
#             return True
#         if(low_str[pointer] != low_str[len(low_str) - pointer - 1]):
#             return False
#         return self.checkReverse(low_str,pointer+1)