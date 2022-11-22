# Time Complexity: O(N)
# Space Complexity: O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Here we keep updating the new interval itself to create a merged interval and add it to the result
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = list()

        # keep track of insertion position
        for insert in range(n):
            # Case 1: Non-overlap: if the current end time is before the starting time of the interval
            if intervals[insert][1] < newInterval[0]:
                res.append(intervals[insert])
            # Case 2: Non-overlap: if the new interval ends before starting of the current
                # we append the newInterval and add all the remaining intervals to res and return
            elif intervals[insert][0] > newInterval[1]:
                res.append(newInterval)
                return res+intervals[insert:]
            # Case 3: There is overlap: we keep updating the newInterval with appropriate
            # start and end if there is overlap so it can be added in the futher iterations
            else:
                newInterval[0] = min(newInterval[0],intervals[insert][0])
                newInterval[1] = max(newInterval[1],intervals[insert][1])
        # if we exit it means we have hit the last index and we just need to append the newinterval
        # to res and return
        res.append(newInterval)
        return res






        # if len(intervals)==0:
        #     intervals.append(newInterval)
        #     return intervals
        # insert = 0
        # while insert<len(intervals):
        #     if intervals[insert][1]<newInterval[0]:
        #         insert+=1
        #         if insert==len(intervals):
        #             intervals.append(newInterval)
        #             return intervals
        #         continue
        #     intervals.insert(insert,newInterval)
        #     j = insert+1
        #     while j<len(intervals) and intervals[j][0]<=intervals[insert][1]:
        #         intervals[insert][0] = min(intervals[insert][0],intervals[j][0])
        #         intervals[insert][1] = max(intervals[insert][1],intervals[j][1])
        #         intervals.pop(j)
        #     break
        # return intervals