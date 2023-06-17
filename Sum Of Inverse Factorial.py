n=int(input("Enter Number:"))
a=1
b=0
for i in range(1,n+1):
    for j in range(1,n+1):
        a*=j
    b+=1/a
    a=1
    n=n-1
print(b)