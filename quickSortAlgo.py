# QUICK SORT ALGORITHM

def partition(arr,low,high): 
	i = ( low - 1)		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i + 1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i + 1 )

def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
print(arr)
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)


# def partition(arr, low, high):
# 	start = low - 1
# 	pivot = high

# 	for i in range(low, high):
# 		if arr[i] <= pivot:
# 			start += 1
# 			arr[start], arr[i] = arr[i], arr[start]
# 	arr[start], arr[high] = arr[high], arr[start]
# 	return start+1

# def quickSort(arr, low, high):
# 	if low < high:
# 		pivot_index = partition(arr, low, high)
# 		quickSort(arr, low, pivot_index-1)
# 		quickSort(arr, pivot_index+1, high)

# # DRIVER CODE
# arr = [11, 9, 29, 7, 2, 15, 28]
# print(arr)
# n = len(arr)
# quickSort(arr, 0, n-1)
# print(arr)