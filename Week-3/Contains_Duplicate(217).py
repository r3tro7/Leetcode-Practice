# Time Complexity: O(N)
# Space Complexity: O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Use a hashset to keep track of all elements
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for elem in nums:
            if elem in dup:
                return True
            else:
                dup.add(elem)
        return False