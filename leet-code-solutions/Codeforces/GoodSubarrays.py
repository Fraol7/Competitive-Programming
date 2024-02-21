from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    prefix, ctr = 0, 0
    refer = defaultdict(int)
    refer[0]= 1
    for i in range(n):
        prefix += int(a[i])
        ctr += refer[prefix-(i + 1)]
        refer[prefix-(i + 1)] += 1
    print(ctr)