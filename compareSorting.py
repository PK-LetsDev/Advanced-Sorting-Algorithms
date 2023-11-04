import time
import random
import matplotlib.pyplot as plt

from merge import merge
from partitioning import partition


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def quickSorting(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSorting(arr, low, pi - 1)
        quickSorting(arr, pi + 1, high)

# Initialize lists to store data
sorting_algorithms = ['Merge Sort', 'Quick Sort']
execution_times = {alg: [] for alg in sorting_algorithms}
data_sizes = list(range(20000, 100001, 20000))

# Test and measure execution times for each sorting method 10 times
num_tests = 10
for n in data_sizes:
    average_times = {alg: 0 for alg in sorting_algorithms}

    for _ in range(num_tests):
        random_integer = random.sample(range(1, n + 1), n)

        for algorithm in sorting_algorithms:
            random_copy = random_integer.copy()
            time_start = time.time()

            if algorithm == 'Merge Sort':
                 mergeSort(random_copy, 0, len(random_copy) - 1)
            elif algorithm == 'Quick Sort':
                quickSorting(random_copy, 0, len(random_copy) - 1)
            
            execution_time = time.time() - time_start
            average_times[algorithm] += execution_time

    for algorithm in sorting_algorithms:
        average_times[algorithm] /= num_tests
        execution_times[algorithm].append(average_times[algorithm])

# Create line charts for each sorting algorithm
for algorithm in sorting_algorithms:
    plt.plot(data_sizes, execution_times[algorithm], marker='o', label=algorithm)

plt.xlabel('Data Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Comparison of Sorting Algorithms (Averaged Over 10 Tests)')
plt.legend()
plt.grid(True)
plt.show()