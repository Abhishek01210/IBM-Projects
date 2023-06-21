def p(a,b):
    if(b==0):
        return 1
    else:
        return a*p(a,b-1)
a=int(input("Enter The Base Value:"))
b=int(input("Enter The Exponent Value:"))
print(p(a,b))