def isSubset(a, b):
    m = len(a)
    n = len(b)
    # Iterate over each element in the second array
    for i in range(n):
        found = False

        # Check if the element exists in the first array
        for j in range(m):
            if b[i] == a[j]:
                found = True
                break

        # If any element is not found, return false
        if not found:
            return False

    # If all elements are found, return true
    return True


if __name__ == "__main__":
    a = [11, 1, 13, 21, 3, 7]
    b = [11, 3, 7, 1]

    if isSubset(a, b):
        print("true")
    else:
        print("false")