# def birthday(s):
#     count = 0  # Initialize result
#     n = len(s)
#     m=2
#     d = 3
#
#     for i in range(0, n):
#         for j in range(i+1, n):
#             if (s[i] + s[j]) == d:
#                 count += 1
#                 count = m
#
#
#     return count
# print(birthday([1, 2, 1, 3, 2]))

# Computes sum all sub-array
# def SubArraySum(arr):
#     temp, result = 0, 0
#     n=len(arr)
#     # Pick starting point
#     for i in range(0, n):
#
#         # Pick ending point
#         temp = 0;
#         for j in range(i, n):
#             # sum subarray between
#             # current starting and
#             # ending points
#             temp += arr[j]
#             result += temp
#     return result
# print(SubArraySum([1,2,3]))
# def search_pairs(array):
#     pairs = []
#     k=3
#     for i in range(len(array)):
#         for i2 in range(i + 1, len(array)):
#             if array[i] + array[i2] == k:
#                # if (array[i], array[i2]) not in pairs and (array[i2], array[i]) not in pairs:
#                     pairs.append((array[i], array[i2]))
#     return pairs
# print(search_pairs([1,2,1,3,2]))
# def birthday(s):
#     x=1
#     count=0
#     m=2
#     n=len(s)
#     d=3
#     while x<=m:
#         for i in range(0, n):
#             for j in range(i + 1, n):
#                 total = s[i] + s[j]
#                 if total == d and x == m:
#                     return n
#             else:
#                 count += 1
#         return count
    #     if x==m:
    #         count +=1
    # else:
    #      x+=1

# # def birthday(s, d, m):
#     count=0
#     n=len(s)
#     x=1
#     while x<=m
#     for i in range(0,n):
#         for j in (i+1,n):
#             if (s[i]+s[j])==d:
#                 count +=1
#     return count
# def birthday(s):
#     count = 0
#     n = len(s)
#     m=2
#     x = len(m)
#     d = 3
#
#     while n <= x:
#         for i in range(0, n):
#             for j in range(i + 1, n):
#                 total = s[i] + s[j]
#                 if total == d:
#
#                     count += 1
#                     break
#         return count
#
#
#
# print(birthday([1,2,1,3,2]))

# def birthday(s, d, m):
#     t=(len(s)-m) +1
#     for i in range(t):
#         if
# def getWays(squares):
#     count = 0
#     d=3
#     m=2
#     for i in range(0,len(squares)-m+1):
#         if sum(squares[i:i+m]) == d:
#             count+=1
#     return count
# print(getWays([1,2,1,3,2]))
def maxSum(arr, k):
    # Initialize result
    #max_sum = INT_MIN
    n=len(arr)
    # Consider all blocks
    # starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]

        # Update result if required.
        max_sum = max(current_sum, max_sum)

    return max_sum
print(maxSum([1, 4, 2, 10, 2, 3, 1, 0, 20],k=4))