#Binary Search Algorithm implementation by Bahram Esmailian

def binary_search(array,target):
    array = sorted(array)
    mid = len(array) // 2

    if len(array) == 0:
        return 'Not Found'
    if array[mid] == target:
        return target
    elif array[mid] > target:
        return binary_search(array[0:mid],target)
    elif array[mid] < target:
        return binary_search(array[mid+1:len(array)],target)

print(binary_search([3,1,8,5,1,20,21,22,23,8,19], 7))
