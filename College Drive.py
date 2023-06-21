print("Welcome To College Campus Drive!")
a=int(input("Enter Your Age:"))
if(a>=18):
    e=int(input("Enter Your Experience:"))
    if(e>1):
        c=input("Enter Your College Name:")
        if(c=="RCE" or c=="RIT"):
            d=input("Enter Your Qualified Course:")
            if(d=="B.Tech" or d=="BCA" or d=="MCA"):
                print("You Are Eligible For Admission")
            else:
                print("Your Degree Is Not Matched")
        else:
            print("Your College Is Not Accepted")
    else:
        print("Your Experience Is Low")
else:
    print("You Are Underage")