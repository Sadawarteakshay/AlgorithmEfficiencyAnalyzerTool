import time
import matplotlib.pyplot as plt

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
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

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
    max_val = max(arr)
    count_arr = [0] * (max_val + 1)
    output_arr = [0] * len(arr)

    for number in arr:
        count_arr[number] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for number in arr:
        output_arr[count_arr[number] - 1] = number
        count_arr[number] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]

# Function to find the median (Order Statistics)
def find_median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 0:
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2
    else:
        return arr_sorted[n // 2]

# Function to measure execution time
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

# Get array size and elements from user
array_size = int(input("Enter the size of the array: "))
user_array = []

for i in range(array_size):
    element = int(input(f"Enter element {i+1}: "))
    user_array.append(element)


# Measure time for sorting the user array
bubble_sort_time = measure_time(bubble_sort, user_array.copy())
insertion_sort_time = measure_time(insertion_sort, user_array.copy())
quick_sort_time = measure_time(quick_sort, user_array.copy())
heap_sort_time = measure_time(heap_sort, user_array.copy())
counting_sort_time = measure_time(counting_sort, user_array.copy())
median = find_median(user_array.copy())

# Display the results
print(f"Bubble Sort Time: {bubble_sort_time} seconds")
print(f"Insertion Sort Time: {insertion_sort_time} seconds")
print(f"Quick Sort Time: {quick_sort_time} seconds")
print(f"Heap Sort Time: {heap_sort_time} seconds")
print(f"Counting Sort Time: {counting_sort_time} seconds")
print(f"Median of Array: {median}")

# Plotting the results
plt.bar(
    ['Bubble Sort', 'Insertion Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort'],
    [bubble_sort_time, insertion_sort_time, quick_sort_time, heap_sort_time, counting_sort_time]
)
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Sorting Algorithm Execution Time')
plt.show()
