def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

nums = [0,5,15,45,7,45,23,6,0,56,100,99,9,63,25,75,22,19,80]
result = selectionSort(nums)
print(result)