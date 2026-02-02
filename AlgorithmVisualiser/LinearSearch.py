def linearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return None

linearSearch([2,3,5,7,1,8,0,10], 7)