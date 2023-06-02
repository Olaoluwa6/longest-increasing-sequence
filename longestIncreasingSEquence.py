def LongestIncreasingSequence(arr):         #an array called arr
    highest = arr[0]            #let the highest element be  the first elemnet 
    lengthOfS = 1               #default length of the sequence be 1
    for i in range(len(arr)):   # iterating over the array until we find an element greater than the first element
        if arr[i] > highest:
            highest = arr[i]
            lengthOfS+=1 

  # code goes here
    return lengthOfS

# keep this function call here 
print(LongestIncreasingSequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]))