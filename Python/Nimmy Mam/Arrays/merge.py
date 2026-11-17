def inpArr():
    li = []
    try:
        while True:
            n = int(input("Enter num: "))
            li.append(n)
    except Exception as e:
        return li

def mergesortdiv(arr,start,end):
    if start >= end:
        return
    mid = (start+end)//2
    mergesortdiv(arr,start,mid)
    mergesortdiv(arr,mid+1,end)
    mergesortmer(arr,start,mid,end)

def mergesortmer(arr,start,mid,end):
    res = []
    i = start
    j = mid + 1
    for k in range(0,(end-start)+1):
        if i <= mid and j <= end:
            if arr[i] < arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        else:
            if i <= mid:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
    for k in range(0,len(res)):
        arr[start] = res[k]
        start += 1

arr = inpArr()
print("Array before MS",arr)
mergesortdiv(arr,0,len(arr)-1)
print("Array after MS",arr)