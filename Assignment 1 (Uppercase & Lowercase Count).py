s=input("Enter Sentence:")
a=0
b=0
for i in range(len(s)):
    if i.isupper==True:
        a+=1
    if i.islower==True:
        b+=1
print("No. Of Uppercase Letters Are:",a)
print("No. Of Lowercase Letters Are:",b)