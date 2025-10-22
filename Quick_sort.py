# o log n
def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []


    for x in arr[-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quickSort(left) + [pivot] + quickSort(right)