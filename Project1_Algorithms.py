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
    count_dict = {}

    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    sorted_arr = []
    for key in sorted(count_dict.keys()):
        sorted_arr.extend([key] * count_dict[key])

    return sorted_arr

def separate_and_sort(arr):
   
    negatives = [abs(num) for num in arr if num < 0]
    positives = [num for num in arr if num >= 0]
    
    sorted_negatives = counting_sort(negatives)
    sorted_positives = counting_sort(positives)

    sorted_negatives=[-abs(num) for num in sorted_negatives][::-1]

    ar=(sorted_negatives+sorted_positives)
    
    for i in range(len(ar)):
        arr[i]=ar[i]

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


def main():
    # Get array size and generate elements randomly
    array_size = int(input("Enter the size of the array: "))
    user_array = [random.randint(-1000, 1000) for i in range(array_size)]
    print("\n Original Array: ", user_array)

    while True:
        print("\nChoose Algorithm:")
        print("1: Bubble Sort")
        print("2: Insertion Sort")
        print("3: Heap Sort")
        print("4: Quick Sort")
        print("5: Counting Sort")
        print("6: Find Median")
        print("7: Selection Sort")
        print("8: Merge Sort")
        print("9: Radix Sort")
        print("10: Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            start_time = time.time()
            bubble_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Bubble Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "2":
            start_time = time.time()
            insertion_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Insertion Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "3":
            start_time = time.time()
            heap_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Heap Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "4":
            start_time = time.time()
            quick_sort(user_array)  # Note: This sorts the array in-place
            end_time = time.time()
            print("\nSorted array using Quick Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "5":
            start_time = time.time()
            counting_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Counting Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "6":
            start_time = time.time()
            median = find_median(user_array)
            end_time = time.time()
            print("\nMedian of the array:", median)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "7":
            start_time = time.time()
            selection_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Selection Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "8":
            start_time = time.time()
            merge_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Merge Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))

        elif choice == "9":
            start_time = time.time()
            radix_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Radix Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))


        elif choice == "10":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()
