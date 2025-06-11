# Function to find the intersection of two arrays
# It returns a list containing the common elements
def intersection(a, b):
    res = []
    m = len(a)
    n = len(b)

    for i in range(m):
      
        # Note that duplicates must be 
        # consecutive in a sorted array
        if i > 0 and a[i - 1] == a[i]:
            continue

        # Since we are only searching distinct
        # elements of a[] in b[] and we break as 
        # soon we find a match, we get only
        # distinct elements in result
        for j in range(n):
            if a[i] == b[j]:
                res.append(a[i])
                break

    return res

# Driver code
a = [3, 5, 10, 10, 10, 15, 15, 20]
b = [5, 10, 10, 15, 30]
res = intersection(a, b)
print(" ".join(map(str, res)))