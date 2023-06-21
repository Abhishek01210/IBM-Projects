def p(s):
    if len(s)==1:
        return True
    else:
        if (s[0]==s[-1]):
            return p(s[1:-1])
        else:
            return False
s=input("Enter The String:")
if(p(s)):
    print("String Is Palindrome")
else:
    print("String Is Not Plaindrome")