class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left:int = 0
        right:int = len(arr) - 1
    
        while(left <= right):
            mid:int = left + ((right - left) // 2)
            
            if((arr[mid] > arr[mid + 1]) and (arr[mid] > arr[mid - 1])):
                return mid
            
            if((arr[mid] > arr[mid + 1]) ):
                right = mid
            else:
                left = mid + 1