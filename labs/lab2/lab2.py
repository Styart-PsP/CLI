def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
      pivot = arr[0]
      less_than_pivot = [x for x in arr[1:] if x <= pivot]
      greater_than_pivot = [x for x in arr[1:] if x > pivot]
      return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

numbers = [1235, 76, 2, 321, 52, 622]
sorted_numbers = quick_sort(numbers)
print("Відсортовані числа:", sorted_numbers)

