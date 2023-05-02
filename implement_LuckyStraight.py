n= input()
l= int(len(n)/2)
left= n[0:l]
right= n[l:]
lResult= 0
rResult= 0
for i in range(l):
    lResult+= int(left[i])
    rResult+= int(right[i])
    
if lResult== rResult:
    print("LUCKY")
else:
    print("READY")