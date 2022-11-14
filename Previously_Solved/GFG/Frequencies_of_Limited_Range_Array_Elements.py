# Given an array A[] of N positive integers which can contain integers from 1 to P 
# where elements can be repeated or can be absent from the array. 
# Your task is to count the frequency of all elements from 1 to N.
# Note: The elements greater than N in the array can be ignored for counting and 
# please read your task section of the problem carefully to understand how to output the array

#Complete the function frequencycount() that takes the array and n as input 
# parameters and modify the array itself in place to denote the frequency 
# count of each element from 1 to N. 
# i,e element at index 0 should represent the frequency of 1 and so on.
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        my_dict = dict()
        
        for i in arr:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        for i in range(1,N+1):
            if i in my_dict:
                arr[i-1] = my_dict[i]
            else:
                arr[i-1] = 0