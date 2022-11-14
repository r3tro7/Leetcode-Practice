class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # left = m - 1
        # right = n -1 
        # position = m + n - 1
        # while (m > 0) and (n > 0):
        while (n >= 1): #left >= 0
            if (m >= 1) and (nums1[m-1] >= nums2[n-1]): #right >= 0
                nums1[m+n-1] = nums1[m-1] #position/write_index
                m -=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
# Link to above solution
# https://leetcode.com/problems/merge-sorted-array/discuss/1176400/Best-Python-Solution-Faster-Than-99-One-Loop-No-Splicing-No-Special-Case-Loop
        
        # Solution 1
        # while (m > 0) and (n > 0):
        #     if(nums1[m-1] >= nums2[n-1]):
        #         nums1[m+n-1] = nums1[m-1]
        #         m -=1
        #     else:
        #         nums1[m+n-1] = nums2[n-1]
        #         n-=1
        # if n > 0:
        #     nums1[:n] = nums2[:n]