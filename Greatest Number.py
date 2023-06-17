a=int(input("Enter The First Number:"))
b=int(input("Enter The Second Number:"))
c=int(input("Enter The Third Number:"))
if(a>b & a>c):
    print("First Number Is Greatest")
elif(b>c & b>a):
    print("Second Number Is Greatest")
else:
    print("Third Number Is Greatest")