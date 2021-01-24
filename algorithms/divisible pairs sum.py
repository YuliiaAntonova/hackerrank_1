def divisibleSumPairs(arr):
    count = 0  # Initialize result
    n=len(arr)
    k=3
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
       for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1

    return count


print(divisibleSumPairs([1, 2, 3, 4, 5, 6]))