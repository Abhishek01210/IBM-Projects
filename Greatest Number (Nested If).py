a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if(a>b):
    if(a>c):
        print("First Number Is Greatest")
elif(b>c):
    if(b>a):
        print("Second Number Is Greatest")
else:
    print("Third Number Is Greatest")
