s= input()
c= int(s[0])
s=s[1:]
move= 0
for i in s:
    i= int(i)
    if c!= i:
        move+=1
        c=i

print(int(move/2))