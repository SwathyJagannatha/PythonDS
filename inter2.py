# Function to find the intersection of two arrays
def intersection(a, b):
    res = []
    m = len(a)
    n = len(b)

    # This is similar to merge of merge sort
    i, j = 0, 0
    while i < m and j < n:

        # Skip duplicate elements in the first array
        if i > 0 and a[i - 1] == a[i]:
            i += 1
            continue

        # Skip the smaller
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1

        # If equal, add to result and move both
        else:
            res.append(a[i])
            i += 1
            j += 1

    return res

# Driver code
a = [3, 5, 10, 10, 10, 15, 15, 20]
b = [5, 10, 10, 15, 30]
res = intersection(a, b)
print(" ".join(map(str, res)))