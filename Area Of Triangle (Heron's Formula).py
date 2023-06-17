from math import *
a=int(input("Enter First Side Of Triangle:"))
b=int(input("Enter Second Side Of Triangle:"))
c=int(input("Enter Third Side Of Triangle:"))
s=(a+b+c)/2
print("Area Of Triangle Is:",sqrt(s*(s-a)*(s-b)*(s-c)))