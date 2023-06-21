n=int(input("Enter The Number:"))
for i in range(65,67+n):
    for j in range(65,i):
        print(chr(j),end="")
    print("")