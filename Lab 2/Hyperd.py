def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1

    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1

def hybrid_merge_sort(arr, left, right, threshold):
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
        return

    if left < right:
        mid = left + (right - left) // 2
        hybrid_merge_sort(arr, left, mid, threshold)
        hybrid_merge_sort(arr, mid + 1, right, threshold)
        merge(arr, left, mid, right)


arr = [38, 27, 43, 3, 9, 82, 10, 50, 21, 29, 15, 4, 7, 55, 40]
threshold = 6  

print("Original array:", arr)
hybrid_merge_sort(arr, 0, len(arr) - 1, threshold)
print("Sorted array:", arr)
