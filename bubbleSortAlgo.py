# BUBBLE SORT IMPLEMENTATION

def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

# DRIVER CODE
arr = [7, 5, 3, 9, 1, 8, 4, 6, 2]
print("array before sorting : ", arr)
bubble_sort(arr)
print("array after sorting : ", arr)


# ANOTHER IMPLEMENTATION
# def bubblesort(arr):
#     length = len(arr)
#     sorted = False
    
#     while not sorted:
#         sorted = True
#         for i in range(length - 1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 sorted = False

# arr = [7, 5, 3, 9, 1, 8, 4, 6, 2]
# print("array before sorting : ", arr)
# bubblesort(arr)
# print("array after sorting : ", arr)