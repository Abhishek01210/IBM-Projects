def s(a):
    if(a<=0):
        return 0
    else:
        return int(a%10)+s(a/10)
a=int(input("Enter The Number:"))
print(s(a))