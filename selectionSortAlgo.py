def min_index(arr, start, end):
    mi = start
    for i in range(start + 1, end):
        if arr[i] < arr[mi]:
            mi = i
    return mi

def selection_sort(arr, arr_size):
    for i in range(arr_size):
        mi = min_index(arr, i, arr_size)
        if i != mi:
            arr[i], arr[mi] = arr[mi], arr[i]

# DRIVER CODE
arr = [5, 1, 6, 8, 2, 3, 7, 9]
print(arr)
selection_sort(arr, len(arr))
print(arr)


# def min_index(arr, start, end):
#     mi = start
#     for i in range(start + 1, end):
#         if arr[i] < arr[mi]:
#             mi = i 
#     return mi

# def selection_sort(arr, arr_size):
#     for i in range(arr_size):
#         mi = min_index(arr, i, arr_size)
#         if i != mi:
#             arr[i], arr[mi] = arr[mi] , arr[i]

# arr = [7, 6, 8, 2, 4]
# print(arr)
# selection_sort(arr, len(arr))
# print(arr)

