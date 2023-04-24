n= int(input())
adventurer= list(map(int, input().split()))
adventurer.sort()
group= 0
i= 0

for g in range(len(adventurer)):
    x= adventurer[i]
    if n<= i+x:
        break
    if adventurer[i+x-1]<=x:
        group+= 1
        i+=x
    else:
        i+=1
        
print(group)