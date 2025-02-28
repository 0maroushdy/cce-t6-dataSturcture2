import random
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000  
array_sizes = [50, 100, 500, 1000, 5000, 10000, 50000, 100000, 150000, 250000]
results = {}
for size in array_sizes:
    arr = generate_random_array(size)
    time_taken = measure_time(bubble_sort, arr.copy())  
    results[size] = time_taken
    print(f"Running time for Bubble Sort with array size {size} is {time_taken:.2f} ms")



    