def insRec(arr,n):
    if n <=1:
        return
    # Sort first n-1 elements
    insRec(arr,n-1)
    
    # '''Insert last element at its correct position in sorted array.'''
    current = arr[n-1]
    position = n - 2
    
    while position >= 0 and arr[position] > current:
        arr[position+1] = arr[position]
        position-=1
    arr[position+1] = current
    

arr = [12,11,3,5,6]
insRec(arr,len(arr))
print(arr)