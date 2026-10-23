n = int(input("Enter num: "))
count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if count < 26:
            print(chr(65 + count), end=" ")
        else:
            print(chr(97 + (count - 26)), end=" ")
        count += 1
        if count == 52:
            count = 0
    print()