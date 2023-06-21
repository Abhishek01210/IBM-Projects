z=int(input("Enter The Beginning Range:"))
x=int(input("Enter The Ending Range:"))
print("Prime Numbers Are:")
for i in range(z,x+1):
    a=0
    for j in range(2,i):
        if(i%j==0):
            a+=1
            break
    if(a==0):
        print(i)