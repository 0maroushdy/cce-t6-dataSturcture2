import random
import time

def selection_sort(array):
    ln = len(array)
    for i in range (ln-1):
        minIndx = i
        for j in range (i+1, ln):
            if array[j] < array[minIndx]:
                minIndx = j
        array[j], array[minIndx] = array[minIndx], array[j]
    return array

# Generating Random array -----------------------------
# arr Sizes: [50, 100, 500, 1000, 5000, 10000, 50000, 100000, 150000, 250000]
siz = 250000
array = [random.randint(0,siz) for _ in range(siz)]

startTime = time.time()
selection_sort(array) 
endTime = time.time()
elTime = endTime - startTime

print(f"The execution time is: {elTime:.4f} seconds, size:{siz}")

