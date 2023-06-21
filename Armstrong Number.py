a=int(input("Enter The Number:"))
b=0
c=0
d=a
while(d>0):
    b=int(d%10)
    d=int(d/10)
    c+=b**3
if(c==a):
    print("Number Is An Armstrong Number")
else:
    print("Number Is Not An Armstrong Number")