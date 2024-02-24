import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Test TimSort by calling Python's built-in sorted function
def timsort(arr):
    return sorted(arr)

# Function to generate random arrays of various sizes
def generate_arrays(sizes):
    arrays = {}
    for size in sizes:
        arrays[size] = [random.randint(0, 1000) for _ in range(size)]
    return arrays

# Function to measure execution time of sorting algorithms
def measure_time(algorithm, arrays):
    times = {}
    for size, arr in arrays.items():
        t = timeit.timeit(lambda: algorithm(arr.copy()), number=1)
        times[size] = t
    return times

# Sizes of arrays to test
sizes = [100, 1000, 10000]

# Generate arrays
arrays = generate_arrays(sizes)

# Measure execution time for each algorithm
merge_times = measure_time(merge_sort, arrays)
insertion_times = measure_time(insertion_sort, arrays)
timsort_times = measure_time(timsort, arrays)

print("Merge Sort Execution Times:")
print(merge_times)
print("\nInsertion Sort Execution Times:")
print(insertion_times)
print("\nTimSort Execution Times:")
print(timsort_times)
