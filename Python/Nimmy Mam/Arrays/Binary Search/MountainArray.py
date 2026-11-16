def IntArray():
    l = []
    while True:
        try:
            n = int(input("Enter num: "))
            l.append(n)
        except Exception as e:
            return l

def FindMountainArray(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] > arr[mid+1]:
            end = mid
        else:
            start = mid+1
    return start

arr = IntArray()
res = FindMountainArray(arr)
print("Array:",arr)
print("Largest elem:",arr[res])
print("Largest elem index:",res)