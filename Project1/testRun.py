from django.shortcuts import render
from .forms import ArrayInputForm
from sorting_algorithms import bubble_sort, quick_sort  # import other algorithms as needed

def sort_array(request):
    sorted_array = []
    if request.method == 'POST':
        form = ArrayInputForm(request.POST)
        if form.is_valid():
            algorithm = form.cleaned_data['algorithm']
            user_array = form.cleaned_data['user_array']
            if algorithm == 'Bubble Sort':
                sorted_array = bubble_sort(user_array)
            elif algorithm == 'Quick Sort':
                sorted_array = quick_sort(user_array)
            # handle other algorithms
            return render(request, 'myapp/sorted_array.html', {'sorted_array': sorted_array})
    else:
        form = ArrayInputForm()
    return render(request, 'myapp/array_input.html', {'form': form})
