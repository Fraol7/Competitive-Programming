n = int(input().strip())
at = map(int, input().strip().split(' '))
a = list(at)

length = len(a)
count = 0
for i in range(length):
    for j in range(length-1):
        if (a[j] > a[j + 1]):
            s = a[j]
            a[j] = a[j+1]
            a[j + 1] = s
            count += 1
print("Array is sorted in",str(count),"swaps.")
print("First Element:",a[0])
print("Last Element:",a[length-1])
