# Time Complexity: O(NlogN)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Here we first sort the array by starting times
# if the start time of the current is before the end time of the previous we return false
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n == 0:
            return True
        intervals.sort()
        end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0] < end:
                return False
            end = intervals[i][1]
        return True


#         if len(intervals)==0:
#             return True
#         high:int = intervals[0][1]
#         for time in intervals:
#             high = max(high,time[1])

#         arr = [0 for _ in range(high+1)]
#         for time in intervals:
#             for x in range(time[0],time[1]):
#                 if arr[x]==0:
#                     arr[x] = 1
#                 else:
#                     return False
#         return True
