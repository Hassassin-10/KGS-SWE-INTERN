def createIntArr():
    l1 = []
    while True:
        try:
            n = int(input("Enter num: "))
            l1.append(n)
        except Exception as e:
            return l1

def binarySearchAsc(arr,target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2

        if target == arr[mid]:
            return mid
        
        if target < arr[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return -1

def binarySearchDsc(arr,target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2

        if target == arr[mid]:
            return mid
        
        if target < arr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return -1

arr = createIntArr()
target = int(input("Enter target elem: "))
print("Created Array: ",arr)
res = binarySearchAsc(arr,target)
if res != 1:
    print("target found at index: ",res)
else:
    print("target not found")