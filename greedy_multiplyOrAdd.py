s= input()
result= int(s[0])
s= s[1:]

for i in s:
    i= int(i)
    if result<1:
        result+= i
    elif i<= 1:
        result+= i
    else:
        result*= i
        
print(result)
