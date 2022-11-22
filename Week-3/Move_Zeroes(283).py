# Time Complexity: O(N)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<2:
            return
        slow = 0
        # We initialize slow to the first zero encountered since we would be swapping that with
        # non-zero elements
        while slow<n:
            if nums[slow] == 0:
                break
            slow+=1
        fast = slow+1

        while fast < n:
            # if fast is a non-zero element we swap elements at fast and slow and increment
            # both pointers
            if nums[fast]!=0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow+=1
            fast+=1     # we need to incremenet fast anyway