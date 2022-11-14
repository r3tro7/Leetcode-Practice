class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # using hashtable/dictionary
        hashtable = {}
        
        for elem in nums:
            if elem in hashtable:
                hashtable[elem] +=1
            else:
                hashtable[elem] = 1
            
        for elem in hashtable:
            if hashtable[elem] == 1:
                return elem


        # using bitwise operators
        # if(len(nums) == 1):
        #     return nums[0]
        
        # final = 0
        # # XOR of any element with itself is 0 -> X^X = 0, 0^X = X
        # for elem in nums:
        #     final ^= elem
            
        # return final