class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start:int = 0
        end:int = len(nums) - 1
        while(end > start):
            mid:int = start + ((end-start)//2)

            if(nums[mid-1] != nums[mid] and nums[mid]!=nums[mid+1]):
                return nums[mid]
            #if mid is even index then the next element should be equal to current
            #if it is not, then search first half of the array
            if(mid%2==0):
                if(nums[mid+1] == nums[mid]):
                    start = mid + 2
                else:
                    end = mid - 1
            else:
                if(nums[mid-1] == nums[mid]):
                    start = mid + 1
                else:
                    end = mid - 2
        return nums[start]