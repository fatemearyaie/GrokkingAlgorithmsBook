# O(Log n)
def binarySearch(arr,target):
    left,right = 0, len(arr) - 1
    while left<=right:
        mid = (left+right)//2
        if mid == target:
            return mid
        if mid < target:
            right = mid + 1
        else:
            left = mid - 1



nums = [1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28,30]
result = binarySearch(nums, 18)
print(result)