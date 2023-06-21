a=int(input("Enter The Number:"))
b=a
c=0
d=0
e=1
while(b>0):
    c=int(b%10)
    b=int(b/10)
    d+=1
while(d>1):
    e*=10
    d-=1
b=a
c=0
d=0
while(b>0):
    c=int(b%10)
    b=int(b/10)
    d+=c*e
    e/=10
if(d==a):
    print("Number Is Palindrome")
else:
    print("Number Is Not Palindrome")
print(d)