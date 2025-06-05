#User function Template for python3


class Solution:

    def countZeroes(self, arr):
        n = len(arr)
        # if the first element is already 0, then all elements are 0, so return n
        if arr[0] == 0:
            return n

        l = 0
        r = n - 1

        # binary search to find the index of the first occurrence of 0 in arr
        while l <= r:
            mid = (l + r) // 2

            # if the mid element is 1, move the left pointer to mid + 1
            if arr[mid] == 1:
                l = mid + 1
            # if the mid element is 0, check if the previous element is also 0
            # if it is, move the right pointer to mid - 1
            # if it is not, return the number of zeroes in the array which is n minus the index of mid
            elif arr[mid] == 0:
                if mid > 0 and arr[mid - 1] == 0:
                    r = mid - 1
                else:
                    return n - mid

        return 0