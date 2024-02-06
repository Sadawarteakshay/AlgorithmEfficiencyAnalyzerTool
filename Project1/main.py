import time
from sorting_algorithms import *

def get_user_array():
    while True:
        user_input = input("Enter the array elements separated by spaces: ")
        try:
            user_array = list(map(int, user_input.split()))
            return user_array
        except ValueError:
            print("Invalid input. Please enter valid integers separated by spaces.")


def main():

    while True:
        print("\nChoose Array Source:")
        print("1: Randomly Generated Array")
        print("2: User Input Array")
        
        array_source_choice = input("Enter your choice (1-2): ")

        if array_source_choice == "1":
            array_size = int(input("Enter the size of the array: "))
            user_array = [random.randint(-1000, 1000) for i in range(array_size)]
            print("\nRandomly Generated Array:", user_array)
            break
        elif array_source_choice == "2":
            user_array = get_user_array()
            print("\nUser Input Array:", user_array)
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 2.")
            continue

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
        print("10: Bucket Sort")
        print("11: Exit")

        choice = input("Enter your choice (1-11): ")

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
            start_time = time.time()
            bucket_sort(user_array)
            end_time = time.time()
            print("\nSorted array using Bucket Sort:", user_array)
            print("Runtime: {:.6f} seconds".format(end_time - start_time))    
        
        
        elif choice == "11":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 11.")

if __name__ == "__main__":
    main()
