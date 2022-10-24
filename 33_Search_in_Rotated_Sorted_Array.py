#Approach 2:Better than pivot
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left:int = 0 
        right:int = len(nums) - 1
        
        while (left <= right):
            
            mid:int = left + ((right - left) // 2)
            if(target == nums[mid]):
                return mid
                
            #check if left part is sorted    
            if(nums[left] <= nums[mid]):
                
                if((target >= nums[left]) and (target < nums[mid])):
                    right = mid - 1
                else:
                    left = mid + 1
                    
            #right sorted part
            else:
                if((target <= nums[right]) and (target > nums[mid])):
                    left = mid + 1
                else:
                    right = mid - 1
            # if(nums[left] <= nums[mid]):
                # if((target > nums[mid]) or (target < nums[left])):
                #     left = mid + 1
                # else:
                #     right = mid - 1
            # else:
                # if((target < nums[mid]) or (target > nums[right])):
                #     right = mid - 1
                # else:
                #     left = mid + 1
                #both work equally just testing both
                    
        return -1


# #Approach 2: Using Pivot Element
# def search(self, nums: List[int], target: int) -> int:
#         pivot:int = self.pivotIndex(nums)
        
#         if(target >= nums[0]):
#             return self.binarySearch(nums, 0, pivot - 1, target)
        
#         return self.binarySearch(nums, pivot, len(nums) - 1, target)
    
#     def pivotIndex(self,nums: List[int]) -> int:
#         low:int = 0
#         high:int = len(nums) - 1
        
#         if(nums[low] <= nums[high]):
#             return (high + 1)
        
#         while(low < high):
#             mid:int = low + ((high - low) // 2)
            
#             if(nums[mid] >= nums[0]):
#                 low = mid + 1
#             else:
#                 high = mid
#         return low
        
#     def binarySearch(self,nums:List[int],low:int,high:int,target:int) -> int:

#         while(low <= high):
#             mid:int = low + ((high - low)//2)
#             if(nums[mid] == target):
#                 return mid
#             elif(target > nums[mid]):
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return -1