y=int(input("Enter The Year:"))
if(y%400==0):
    print("The Year Is Leap Year")
elif(y%100):
    if(y%100==0):
        print("Year Is Not Leap Year")
    elif(y%100!=0 & y%4==0):
        print("Year Is Leap Year")
else:
    print("Year Is Not Leap Year")