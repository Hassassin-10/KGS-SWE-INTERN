def createIntArr():
    l1 = []
    while True:
        try:
            n = int(input("Enter num: "))
            l1.append(n)
        except Exception as e:
            return l1

def binarySearch(arr,target):
    start = 0
    end = len(arr)-1
    flag = "asc"
    if arr[start] > arr[end]:
        flag = "dsc"
    if flag=="asc":
        while start <= end:
            mid = (start+end)//2

            if target == arr[mid]:
                return mid
        
            if target < arr[mid]:
                end = mid - 1

            else:
                start = mid + 1
        return -1
    else:
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
res = binarySearch(arr,target)
if res != 1:
    print("target found at index: ",res)
else:
    print("target not found")