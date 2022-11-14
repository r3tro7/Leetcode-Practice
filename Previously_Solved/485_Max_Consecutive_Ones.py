class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_o = 0
        count = 0
        
        for i in range(len(nums)):
            if(nums[i] == 1):
                count += 1
            else:
                if(count > max_o):
                    max_o = count
                count = 0
            
            if(count > max_o):
                max_o = count
                
            # if(nums[i] != 1):
            #     count = 0
            #     continue
            # count+=1
            # if(count > max_o):
            #     max_o = count
            
        return max_o
            