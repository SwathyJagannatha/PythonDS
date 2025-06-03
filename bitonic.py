# Python program to find bitonic point in an array
# using linear search

# function to find the maximum element 
def findMaximum(arr):
    mx = arr[0]
    for i in range(1, len(arr)):
        
        # update max when found greater value
        if arr[i] > mx:
            mx = arr[i]
        
        # break when once an element is smaller than 
        # the max then it will go on decreasing 
        # and no need to check after that 
        else:
            break
    return mx

if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 3]
    print(findMaximum(arr))