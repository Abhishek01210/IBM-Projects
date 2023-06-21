s=input("Enter Sentence:")
a=b=c=0
for i in s:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        b+=1
    else:
        c+=1
print(a,b,c)