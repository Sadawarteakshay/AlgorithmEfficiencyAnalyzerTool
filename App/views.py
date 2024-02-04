# from django.shortcuts import render
# from django.http import HttpResponse
# # views.py

from django.shortcuts import render
from django.http import HttpResponse
from .sorting_algorithms import bubble_sort, merge_sort, insertion_sort

# # Create your views here.

# def initiate(request):
#     return render(request, 'index.html')

# views.py

def analyze_algorithm(request):
    if request.method == 'POST':
        numbers = request.POST.get('numbers')  # Get the input numbers from the form
        bubble_sort_checkbox = request.POST.get('bubble_sort')  # Get the checkbox value for Bubble Sort
        merge_sort_checkbox = request.POST.get('merge_sort')  # Get the checkbox value for Merge Sort
        insertion_sort_checkbox = request.POST.get('insertion_sort')  # Get the checkbox value for Insertion Sort

        # Process the input numbers (convert to list, parse, etc.)
        print(numbers)
        numbers_list = [int(num.strip()) for num in numbers.split('%2C')]
       
        print(*numbers_list, sep = "\n")

        # Call sorting algorithm functions based on checkbox values
        if bubble_sort_checkbox:
            bubble_sort(numbers_list)
        if merge_sort_checkbox:
            merge_sort(numbers_list)
        if insertion_sort_checkbox:
            insertion_sort(numbers_list)

        # Return the sorted list or any other result as needed
        sorted_result = ', '.join(str(num) for num in numbers_list)
        return HttpResponse(f"Sorted Result: {sorted_result}")

    else:
        # Handle GET request if needed
        return render(request, 'index.html')  # Replace 'your_template.html' with the actual template name


