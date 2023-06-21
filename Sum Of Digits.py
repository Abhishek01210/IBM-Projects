a=int(input("Enter The Number:"))
b=0
c=0
while(a>0):
    b=int(a%10)
    a=int(a/10)
    c+=b
print(c)    