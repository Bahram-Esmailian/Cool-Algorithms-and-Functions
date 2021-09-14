#A Quick Sorting Algorim created and written by Bahram Esmailian

def QuickSort(arr):
	if len(arr) < 2:
		return arr
	pivot = arr[0]
	index = 0
	for n in range(1, len(arr)):
		if arr[n] <= pivot:
			index += 1
			arr[n], arr[index] = arr[index], arr[n]
			print(arr)
	arr[0], arr[index] = arr[index], arr[0]
	left = QuickSort(arr[0:index])
	right = QuickSort(arr[index+1:len(arr)])
	return left + [arr[index]] + right

print(QuickSort([3,2,1,4,5]))
