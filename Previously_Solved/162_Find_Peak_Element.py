class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while(start < end):
            mid = start + ((end - start)//2)
            #this will not go out of bounds as 
            #it only goes out of bounds if end == start
            #but here we are dodging that case entirely
            if(nums[mid] > nums[mid+1]):
                end = mid
            else:
                start = mid+1
        return end