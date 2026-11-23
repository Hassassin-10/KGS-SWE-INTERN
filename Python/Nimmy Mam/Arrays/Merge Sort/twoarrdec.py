arr1 = [99, 96, 86, 80, 70, 69, 50]
arr2 = [100, 95, 85, 82]

def MergeTwoDec(arr1, arr2):
    i, j = 0,0
    n1, n2 = len(arr1), len(arr2)
    res = []
    k = 0
    while k < (n1+n2):
        if i < n1 and j < n2:
            if arr1[i] > arr2[j]:
                res.append(arr1[i])
                i += 1
                k+=1
            else:
                res.append(arr2[j])
                j += 1
                k+=1

        elif i < n1:
            res.append(arr1[i])
            i += 1
            k+=1

        elif j < n2:
            res.append(arr2[j])
            j += 1
            k+=1

    return res
print(MergeTwoDec(arr1, arr2))