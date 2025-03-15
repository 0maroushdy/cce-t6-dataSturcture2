import random
import time

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(array):
    n = len(array)
    build_max_heap(array)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heapify(array, i, 0)

def generate_random_array(size):
    return [random.randint(0,size) for _ in range(size)]

def measure_time(sort_function,array):
    start_time = time.time()
    sort_function(array)
    end_time = time.time()
    return (end_time - start_time)*1000

array_sizes = [50,100,500,1000,5000,10000,50000,100000]

for size in array_sizes:
    array = generate_random_array(size)
    time_taken1 = measure_time(bubble_sort, array.copy())
    time_taken2 = measure_time(insertion_sort, array.copy())
    time_taken3 = measure_time(selection_sort, array.copy())
    time_taken4 = measure_time(quick_sort, array.copy())
    time_taken5 = measure_time(merge_sort, array.copy())
    time_taken6 = measure_time(heap_sort, array.copy())
    print(f"Running Time for Bubble Sort of array size {size}: {time_taken1:.2f}ms")
    print(f"Running Time for Insertion Sort of array size {size}: {time_taken2:.2f}ms")
    print(f"Running Time for Selection Sort of array size {size}: {time_taken3:.2f}ms")
    print(f"Running Time for Quick Sort of array size {size}: {time_taken4:.2f}ms")
    print(f"Running Time for Merge Sort of array size {size}: {time_taken5:.2f}ms")
    print(f"Running Time for Heap Sort of array size {size}: {time_taken6:.2f}ms")
    print()
    print("------------------------------------")