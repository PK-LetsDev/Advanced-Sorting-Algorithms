import random
import time

from partitioning import partition


def quickSorting(arr, low, high):
    print("arr =", arr)
    if low < high:
        pi = partition(arr, low, high)

        quickSorting(arr, low, pi - 1)
        quickSorting(arr, pi + 1, high)


n = 100000
random_integers = random.sample(range(1, n+1), n)
# print(random_integers)

start_time = time.time()
quickSorting(random_integers, 0, len(random_integers)-1)
end_time = time.time()
print(random_integers)

print("Start time:", start_time)
print("End time:", end_time)
print("Quick Sorting time:", end_time - start_time)


# test = [42, 89, 63, 12, 94, 27, 78, 3, 50, 36]
# quickSorting(test, 0, len(test) - 1)
# print(test)


# Find from left to right both i & j.
# pi is pivot

# [42i, 89, 63, 12j, 94, 27, 78, 3, 50, 36pi]
# [12, 89i, 63, 42, 94, 27j, 78, 3, 50, 36pi]
# [12, 27, 63i, 42, 94, 89, 78, 3j, 50, 36pi]
# [12, 27, 3, 42i, 94, 89, 78, 63, 50, 36pi,j]
# [12, 27, 3, 36, 94, 89, 78, 63, 50, 42]

# [12, 27, 3, 36, 94, 89, 78, 63, 50, 42]
# [12, 27, 3][36][94, 89, 78, 63, 50, 42]
# [12ij, 27, 3pi][36][94, 89, 78, 63, 50, 42]
# [12i, 27, 3pi,j][36][94, 89, 78, 63, 50, 42]
# [3, 27, 12][36][94, 89, 78, 63, 50, 42]
# [3][27i, 12pi,j][36][94, 89, 78, 63, 50, 42]
# [3][12, 27][36][94, 89, 78, 63, 50, 42]

# [3, 12, 27, 36][94ij, 89, 78, 63, 50, 42pi]
# [3, 12, 27, 36][94i, 89, 78, 63, 50, 42pi,j]
# [3, 12, 27, 36][42, 89, 78, 63, 50, 94]

# [3, 12, 27, 36, 42][89, 78, 63, 50][94]
# [3, 12, 27, 36, 42][89ij, 78, 63, 50pi][94]
# [3, 12, 27, 36, 42][89i, 78, 63, 50pi,j][94]
# [3, 12, 27, 36, 42][50, 78, 63, 89][94]
# [3, 12, 27, 36, 42, 50][78, 63][89, 94]
# [3, 12, 27, 36, 42, 50][78i, 63pi,j][89, 94]
# [3, 12, 27, 36, 42, 50][63, 78, 89, 94]
# [3, 12, 27, 36, 42, 50, 63, 78, 89, 94]


