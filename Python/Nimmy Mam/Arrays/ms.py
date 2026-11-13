arr = [8, 3, 5, 2, 9, 1]

def mergesortdiv(arr,start,end):
    if start >= end:
        return
    mid = (start+end) // 2
    mergesortdiv(arr,start,mid)
    mergesortdiv(arr,mid+1,end)
    mergesortmerge(arr,start,mid,end)

def mergesortmerge(arr,start,mid,end):
    res = []
    i = start
    j = mid+1
    while i <= mid and j <= end:
        pass