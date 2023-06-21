l=[1,2,3,4,5,6,7,8]
a=eval(input("Enter The Element You Want To Find:"))
for i in range(len(l)):
    if(l[i]==a):
        print("Element Found At Index",i)
        break
else:
    print("Element Not Found")