def missingNumber( A, N):
    # Your code goes here
    total = 0
    for i in range(1,N+1):
        total += i
    for elem in A:
        total -= elem
    return total