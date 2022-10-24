class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        start = 0
        while(start<len(nums)):
            if(nums[start]==0):
                break
            else:
                start += 1
        # start is the first occurence of 0 in the array
        right = start+1
        # traverse till the first occurence of non-zero in right and swap
        while((start < len(nums)) and (right < len(nums))):
            if(nums[right] != 0):
                nums[start] , nums[right] = nums[right], nums[start]
                start+=1
            right+=1
        