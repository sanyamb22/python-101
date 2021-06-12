# Merge Function
def merge(left_arr, right_arr):
    i, j = 0, 0
    result = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1
    result += left_arr[i:]
    result += right_arr[j:]
    return result

# Merge Sort Function
def merge_sort(lst):
    if len(lst) <= 1 :
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

# Driver code
arr = [2, 8, 4, 9, 7, 3, 5, 1]
print("Array before sorting :", arr)
print("Array after sorting : ",merge_sort(arr))




# def merge(left_arr, right_arr):
#     i, j = 0, 0
#     result = []
#     while i < len(left_arr) and j < len(right_arr):
#         if left_arr[i] <= right_arr[j]:
#             result.append(left_arr[i])
#             i+=1
#         else:
#             result.append(right_arr[j])
#             j+=1
#     result += left_arr[i:]
#     result += right_arr[j:]
#     return result

# def mergeSort(lst):
#     if len(lst) <= 1:
#         return lst
#     mid = len(lst)//2
#     left = mergeSort(lst[:mid])
#     right = mergeSort(lst[mid:])
#     return merge(left, right)

# arr = [2, 8, 7, 6, 3, 4, 5, 1]     
# print(arr)
# print(mergeSort(arr))  