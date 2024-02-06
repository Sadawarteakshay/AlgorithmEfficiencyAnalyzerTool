def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range (low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if len(arr) <= 1:
        return arr
    elif low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    try:
        arr = list(map(int, input("Enter number seperated by spaces: ").split()))
        quick_sort(arr, 0, len(arr) - 1)
        print("Sorted Array: ", arr)
    except ValueError:
        print("Please enter only integers seperateed by spaces")    

if __name__ == '__main__':
    main()
