class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first:int = self.findOcc(nums, target, True)
        last:int = self.findOcc(nums, target, False)
        return [first, last]
        
    def findOcc(self, nums: List[int], target, find_start_index:bool):
        ans:int = -1
        start:int = 0
        end:int = len(nums) - 1
        while(start <= end):
            mid:int = start + ((end - start)//2)
            if(target > nums[mid]):
                start = mid + 1
            elif(target < nums[mid]):
                end = mid - 1
            else:
                ans = mid
                if(find_start_index):
                    end = mid - 1
                else:
                    start = mid + 1
        return ans