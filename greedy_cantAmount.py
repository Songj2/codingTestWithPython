n= int(input())
unit= list(map(int, input().split()))
unit.sort()
result= unit
c= 0
for i in range(n):
    for j in range(i+1, n):
        result.append(result[i+c]+unit[j])
        c+=1


result.sort()
result=list(set(result))

for i in range(len(result)):
    if i != result[i]-1:
        print(result[i]-1)
        break

