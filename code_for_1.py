num, low, hi= map(int,input().split())
List = []
def code_41(num):
    if num <= 1:
        List.append(num)
    else:
        List.append(num%2)
        code_41(num//2)
        List.reverse()
code_41(num)
answer = []
for i in range(len(List)):
    answer.append(List[i])
    if i != 0:
        length = len(answer)-1 
        answer = answer + answer[:length]
ctr = 0
for j in answer[low-1:hi]:
    if j == 1:
        ctr += 1
print(ctr)
