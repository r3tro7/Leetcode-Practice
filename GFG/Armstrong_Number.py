# For a given 3 digit number, find whether it is armstrong number or not. 
# An Armstrong number of three digits is an integer such that the 
# sum of the cubes of its digits is equal to the number itself. 
# Return "Yes" if it is a armstrong number else return "No".
# NOTE: 371 is an Armstrong number since 33 + 73 + 13 = 371

# Example 1:

# Input: N = 153
# Output: "Yes"
# Explanation: 153 is an Armstrong number
# since 13 + 53 + 33 = 153.
# Hence answer is "Yes".



class Solution:
    def armstrongNumber (ob, n):
        # code here 
        power = len(str(n))
        num = n
        total = 0
        while(num):
            total += pow((num%10), power)
            num //= 10
        if(total == n):
            return "Yes"
        else:
            return "No"