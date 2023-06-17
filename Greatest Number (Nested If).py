a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if(a>b):
    if(a>c):
        print(a,"Is Greatest Number")
elif(b>a):
    if(b>c):
        print(b,"Is Greatest Number")
else:
    print(c,"Is Greatest Number")