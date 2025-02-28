import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j>0:
            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            j -=1

arr = [random.randint(0,50000) for _ in range(50000)]

startTime = time.time()

insertion_sort(arr)

endTime = time.time()
elapsedTime = endTime - startTime

print(f"Execution time: {elapsedTime:.3f} seconds")

