# Given a number N. Count the number of digits in N which evenly divides N.
# Example 1:

# Input:
# N = 12
# Output:
# 2
# Explanation:
# 1, 2 both divide 12 evenly

# Example 2:

# Input:
# N = 23
# Output
# 0
# Explanation:
# 2 and 3, none of them
# divide 23 evenly

class Solution:
    def evenlyDivides (self, N):
        # code here
        num = N
        count = 0
        while(num >0):
            rem = num%10
            num = num//10
            if(rem == 0):
                continue
            if(N%rem == 0):
                count+=1
        return count
