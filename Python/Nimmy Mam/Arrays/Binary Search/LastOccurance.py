def createIntArr():
    l1 = []
    while True:
        try:
            n = int(input("Enter num: "))
            l1.append(n)
        except Exception as e:
            return l1

def LastOccur(arr,target):
    start = 0
    end = len(arr)-1
    lastOcc = -1
    while start <= end:
        mid = (start+end)//2
        if target >= arr[mid]:
            lastOcc = mid
            start = mid + 1
        else:
            end = mid - 1
    return lastOcc

arr = createIntArr()
target = int(input("Enter target elem: "))
print("Created Array: ",arr)
res = LastOccur(arr,target)
if res == -1:
    print("target not found")
else:
    print("first occur in index:",res)