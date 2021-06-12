# INSERTION SORT ALGORITHM

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key <= arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key

# driver code
arr = [12, 11, 13, 8, 10]
print("array before sorting :",arr)
insertionSort(arr)
print("sorted array is :", arr)

# for i in range(len(arr)):
#     print(arr[i])


# OTHER IMPLEMENTATION


# def insertion_sort(list_a):
#     indexing_length = range(1, len(list_a))
#     for i in indexing_length:
#         value_to_sort = list_a[i]

#         while list_a[i-1] > value_to_sort and i > 0:
#             list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
#             i = i -1

#     return list_a

# print(insertion_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8]))



# def insSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while arr[j] >= key and j >= 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             j = j - 1
#     arr[j+1] = key

# arr = [4, 8, 6, 7, 10, 44, 15]
# print(arr)
# insSort(arr)
# print(arr)
