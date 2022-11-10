# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low:int = 0
        high:int = n

        while low < high:
            mid:int = low + ((high - low)//2)

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high