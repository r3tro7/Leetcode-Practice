#Approach: Find pivot element and return next element

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low:int = 0
        high:int = len(nums) - 1
        
        if(nums[low] <= nums[high]):
            return nums[low]
        
        while(low < high):
            mid:int = low + ((high - low) // 2)
            
            if(nums[mid] >= nums[0]):
                low = mid + 1
            else:
                high = mid
        return nums[low]