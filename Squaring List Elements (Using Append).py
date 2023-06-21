a=eval(input("Enter The List:"))
b=[]
for i in range(len(a)):
    b.append(a[i]*a[i])
print(b)