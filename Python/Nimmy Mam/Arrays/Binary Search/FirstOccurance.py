def createIntArr():
    l1 = []
    while True:
        try:
            n = int(input("Enter num: "))
            l1.append(n)
        except Exception as e:
            return l1

def FirstOccur(arr,target):
    start = 0
    end = len(arr)-1
    firstOcc = -1
    while start <= end:
        mid = (start+end)//2
        if target <= arr[mid]:
            firstOcc = mid
            end = mid - 1
        else:
            start = mid + 1
    return firstOcc

arr = createIntArr()
target = int(input("Enter target elem: "))
print("Created Array: ",arr)
res = FirstOccur(arr,target)
if res == -1:
    print("target not found")
else:
    print("first occur in index:",res)