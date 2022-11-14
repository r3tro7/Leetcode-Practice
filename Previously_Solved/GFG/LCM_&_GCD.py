# Given two numbers A and B. The task is to find out their LCM and GCD.
# Example 1:

# Input:
# A = 5 , B = 10
# Output:
# 10 5
# Explanation:
# LCM of 5 and 10 is 10, while
# thier GCD is 5.

class Solution:
    # def compute_gcd(num1 , num2):
    #     while num2:
    #         num1,num2 = num2, num1%num2
    #     return num1
        
    # def compute_lcm(num1 , num2):
    #     return ((num1*num2)//compute_gcd(num1,num2))
        
    def lcmAndGcd(self, A , B):
        # code here 
        num1,num2 = A,B
        while num2:
            num1,num2 = num2, num1%num2
        gcd = num1
        lcm = A*B // gcd
        return lcm,gcd