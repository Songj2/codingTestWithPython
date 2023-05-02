n, m= map(int, input().split())

weight= list(map(int, input().split()))
result= 0
for i in range(n):
    s= weight[i]
    for j in range(i, n):
        if s!= weight[j]:
            result+= 1

print(result)