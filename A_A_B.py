t = int(input())
for _ in range(t):
    opr = list(int(x) for x in input().split('+'))
    a, b = opr[0], opr[1]
    print(a+b)
