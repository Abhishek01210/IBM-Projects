print("Welcome To Blood Donation Camp")
a=int(input("Enter Your Age:"))
if(a>=19):
    w=int(input("Enter Your Weight:"))
    if(w>=45):
        h=int(input("Enter Your Height:"))
        if(h>=173):
            b=input("Enter Your Blood Group:")
            if(b=="O+" or b=="O-" or b=="B+" or b=="B-" or b=="o+" or b=="o-" or b=="b+" or b=="b-"):
                print("You Are ELigible For Blood Donation")
            else:
                print("Your Blood Group Is Not Accepted")
        else:
            print("You Height Doesn't Meet The Condition")
    else:
        print("You Are Underweight")
else:
    print("You Are Underage")    