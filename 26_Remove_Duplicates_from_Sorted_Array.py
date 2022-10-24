class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        position = 0
        for i in range(1,len(nums)):
            if(nums[position] != nums[i]):
                position+=1
                nums[position] = nums[i]
        return position+1


        # First thought
        # position = 0
        # scan = 1
        # while(scan<len(nums)):
        #     if(nums[position] == nums[scan]):
        #         scan+=1
        #         continue
            
        #     position+=1
        #     nums[position] = nums[scan]
        #     scan+=1
        # return position+1
        