# Time Complexity: O(N)
# Space Complexity: O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(n)]
        left = 0
        right = n-1
        end = n-1

        # Here we start appeding from the end as it is easier to keep track of largest element
        # we append the square of the larger element from left and right and ++/-- the respective pointer
        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                res[end] = pow(nums[left],2)
                left+=1
            else:
                res[end] = pow(nums[right],2)
                right-=1
            end-=1
        return res