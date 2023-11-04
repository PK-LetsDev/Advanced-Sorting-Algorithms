import random
import time
from merge import merge


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

# test = [42, 89, 63, 12, 94, 27, 78, 3, 50, 36]
# mergeSort(test, 0, len(test)- 1)
# print(test)

n = 100000
random_integers = random.sample(range(1, n+1), n)
# print(random_integers)

start_time = time.time()
mergeSort(random_integers, 0, len(random_integers)- 1)
end_time = time.time()
print(random_integers)

print("Start time:", start_time)
print("End time:", end_time)
print("Quick Sorting time:", end_time - start_time)


