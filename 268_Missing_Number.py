class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = 0
        for i in range(1,len(nums)+1):
            total += i
        # total = (len(nums) * (len(nums)+1))//2 
        
        for elem in nums:
            total -= elem
        return total
        