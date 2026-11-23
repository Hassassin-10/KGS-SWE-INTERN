l1 = [2,4,3] 
l2 = [5,6,4]

def SumNode(l1,l2):
    l1 = l1[::-1]
    l2 = l2[::-1]
    s1,s2 = 0,0
    for i in l1:
        s1 = (s1 * 10) + i
    for j in l2:
        s2 = (s2 * 10) + j
    sum = s1+s2
    l = [int(digit) for digit in str(sum)][::-1]
    return l

res = SumNode(l1,l2)
print(res)