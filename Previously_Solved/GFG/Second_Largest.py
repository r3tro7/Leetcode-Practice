import sys
class Solution:

    def print2largest(self,arr, n):
    # code here
        if(n<2):
            return -1
        max_e = arr[0]
        second_e = -sys.maxsize - 1

        for elem in arr:
            if elem > max_e:
                second_e = max_e
                max_e = elem
            elif elem > second_e and elem != max_e:
                second_e = elem

        if second_e > -sys.maxsize - 1:
            return second_e
        else:
            return -1




        #Solution 1
    # for elem in arr:
    #     if elem > max_e:
    #         max_e = elem
    # for elem in arr:
    #     if elem > second_e and elem < max_e:
    #         second_e = elem
            
    # if second_e > -sys.maxsize - 1:
    #     return second_e
    # else:
    #     return -1