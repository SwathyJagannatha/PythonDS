class Solution:
    # Function to find floor of x in sorted array arr
    # Returns index of floor element or -1 if it doesn't exist
    def findFloor(self, arr, x):
        n = len(arr)

        low, high = 0, n - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] <= x:
                ans = mid  # Potential floor found
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half

        return ans  # Index of largest element <= x, or -1 if no floor