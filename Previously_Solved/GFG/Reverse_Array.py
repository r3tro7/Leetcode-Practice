#First line contains an integer denoting the test cases 'T'. 
# T testcases follow. Each testcase contains two lines of input. 
# First line contains N the size of the array A. 
# The second line contains the elements of the array.


def rev_array(begin,end,arr):
    if(begin>end):
        return
    # swap(begin,end)
    arr[begin],arr[end] = arr[end],arr[begin]
    rev_array(begin+1,end-1,arr)

testcases = int(input())
for i in range(testcases):
    test_size = int(input())
    # arr = list()
    # for _ in range(test_size):
    #     ele = int(input())
    #     arr.append(ele)
    
    arr = list(map(int,input().strip().split()))[:test_size]
    # print(arr)
    # print(test_size)
    rev_array(0,test_size-1,arr)
    # print(*rev_array(0,test_size-1,arr))
    print(*arr)