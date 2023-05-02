food_times= 	[3, 2, 5, 8]
k= 10

l= len(food_times)
ind= 0
time= 0
while time<=k:

    if max(food_times)<1:
        result= -1
        break
        
    if food_times[ind]>0:
        food_times[ind]-= 1
        time+=1
        if time<=k:
            ind= (ind+ 1)%l
    else:

        ind=(ind + 1) %l
        
    
    
print(ind+1)
# 27번 타임 아웃
