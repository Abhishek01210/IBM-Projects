a=int(input("Enter The Number:"))
b=0
for i in range(2,a):
    if(a%i==0):
        b+=1
        break
if(b==0):
    print("Number Is Prime Number")
else:
    print("It Is Not A Prime Number")