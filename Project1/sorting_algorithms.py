import time
import random

# Bubble Sort Function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort Function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Quick Sort Function
def quick_sort(arr):
    def _quick_sort(items, low, high):
        while low < high:
            pivot_index = partition(items, low, high)
            if pivot_index - low < high - pivot_index:
                _quick_sort(items, low, pivot_index - 1)
                low = pivot_index + 1
            else:
                _quick_sort(items, pivot_index + 1, high)
                high = pivot_index - 1

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)


# Heap Sort Function
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Counting Sort Function

def counting_sort(arr):

    n=len(arr)
    
    min_val = min(arr)
    max_val = max(arr)

    count = [0] * (max_val - min_val + 1)

    offset = -min_val

    for num in arr:
        count[num + offset] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sorted_arr = [0] * n
    for num in reversed(arr):
        sorted_arr[count[num + offset] - 1] = num
        count[num + offset] -= 1

    for i in range(n):
        arr[i]=sorted_arr[i]
        
    return arr


# Find Median Function
def find_median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 0:
        return arr_sorted[n // 2]
    else:
        return arr_sorted[n // 2]
    
# Selection Sort Function
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge Sort Function
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

# Radix Sort Function
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 20 

    for i in range(n):
        index = (arr[i] // exp) + 10
        count[index % 20] += 1

    for i in range(1, 20):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) + 10
        output[count[index % 20] - 1] = arr[i]
        count[index % 20] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Bucket Sort Function
def bucket_sort(arr):
    if not arr:
        return arr

    min_val, max_val = min(arr), max(arr)
    range_val = max_val - min_val + 1

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val) * (len(arr) - 1) / range_val)
        buckets[index].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    k = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr

# Quickselect Function
def quickselect(arr, k):
    if not arr:
        return None
    pivot = random.choice(arr)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    kth_smallest = len(low)
    if k < kth_smallest:
        return quickselect(low, k)
    elif k > kth_smallest:
        return quickselect(high, k - kth_smallest - 1)
    else:
        return pivot

