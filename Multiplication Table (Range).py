a=int(input("Enter The Beginning Number:"))
b=int(input("Enter The Ending Number:"))
for i in range(a,b+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
        