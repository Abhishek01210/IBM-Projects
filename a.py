#strings--------------------------------------------------------------------------------------------
s="abc 123$%"
print(s.capitalize())
print(s.upper())
print(s.isupper())
print(s.islower())
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())
print(s.isspace())
print("*".join(s))
#print(s.split(''))
#lists------------------------------------------------------------------------------------------------------
a=list((1,2,3,4,5))
print(a[2])
a=(1,2,3,4,5)
print(a[2])
l1=[1,2,3]
l2=["a","True","3+4j"]
print(l1+l2)
print(l1*3)
l1=["apple","kiwi","banana"]
l2=["apple","kiwi","Banana"]
print(l1<l2)
print(l2<l1)
print(l2==l1)
l=[1,2,3,4]
for i in l:
    print(i)
for i in range(0,len(l)):
    print(l[i])
print(len(l))
s="Hello"
print(list(s))
#a=eval(input("Enter The List Elements:"))
#print(a)
l=[1,2,2,3,True]
l[1]="Hello"
print(l)
l=[1,2,3,"Hello"]
l.append([23,67,89])
l.extend([34,56,78,True])
print(l)
del l[3]
print(l)
print(l.pop())
print(l)
#del deletes the element at mentioned index
#pop deletes the element at mentioned index and returns the value
l=[1,2,2,3,4,2,2,"Hello"]
print(l.count(2))
#count returns the occurence of element
print(l.index("Hello"))
l.insert(3,40)
print(l)
l=[1,2,3,2,8,5]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
l.remove(2)
print(l)
l.remove(2)
print(l)
l=[1,2,3,4]
print(5 in l)
print(5 not in l)
l1=[1,2,3]
l2=[1,2,3]
print(id(l1))
print(id(l2))
print(l1 is l2)
print(l1 is not l2)
#tuple----------------------------------------------------------------------------------------------------------------------
t=(1,2,3,4,"Hello")
t2=tuple((1,2,3,"Hello"))
print(t)
print(t2)
#print(max(t))
#print(min(t))
#tuple unpacking------------------------------------------------------------------------------------------------------------
fruits={"mango","apple","orange"}
print(fruits)
print("mango" in fruits)
for i in fruits:
    print(i)
fruits.add("kiwi")
print(fruits)
#fruits.update("banana","cherry","watermeleon")
#print(fruits)
print(len(fruits))
#fruits.clear()
#print(fruits)
#fruits.remove("mango")
#print(fruits)
#print(fruits.pop())
#del fruits
#print(fruits)
fruits1={"mango","kiwi","apple"}
fruits2={"orange","watermeleon"}
fruits3=fruits1.union(fruits2)
print(fruits3)
fruits3=fruits1.intersection(fruits2)
print(fruits3)
#sets----------------------------------------------------------------------------------------------------------
set1={1,2,3,4}
set2={1,2,3}
print(set1.issuperset(set2))
set2=set1.copy()
print(set2)
set3=set1.difference(set2)
print(set3)
d={"a":1,"b":2,"c":3}
print(d)
#print(d["b"])
for key in d:
    print(d[key])
    print(key,"->",d[key])
print(len(d))
print(d.keys())
print(d.values())
del d["b"]
print(d)
#print(d.pop("b"))
print(d.items())
#d.clear()
#print(d)
d1={"a":1,"b":2,"c":3}
d2={"j":4,"k":5,"l":6}
d1.update(d2)
print(d1)
#functions-------------------------------------------------------------------------------------------------
'''def demo(name):
    print(name)
n=input("Enter The Name:")
demo(n)'''
def demo():
    return 2,8
n,t=demo()
print(n,t)
#Local And Global Variables-----------------------------------------------------------------------------------------
a=10
def demo():
    global a
    a=a+2
    print(a)
demo()
def demo(a=10):
    print(a)
demo()
demo(4)
def demo(*args):
    print(*args)
demo(4,5,6,7,8,9)
#recursion------------------------------------------------------------------------------------------------------------------------
def f(n):
    if(n==0):
        return 1
    else:
        return n*f(n-1)
print(f(6))
#lambda------------------------------------------------------------------------------------------------------------------------------
result=lambda x:x+5
print(result(5))
l=[1,2,3,4,5]
result=map(lambda x:x**2,l)
print(list(result))
l=[12,45,67,66,89]
result=filter(lambda x:x%2==0,l)
print(list(result))
from functools import reduce
l=[1,2,3,4,5,7]
r=reduce(lambda x,y:x+y,l)
print(r)
n=[5,6,7,8,9,10]
r=reduce(lambda x,y:max(x,y),n)
print(r)
r=reduce(lambda x,y:x if x>y else y,n)
print(r)
l=[{'make':'Nokia','model':216,'color':'black'},{'make':'Mi Max','model':2,'color':'Gold'},{'make':'Samsung','model':7,'color':'Blue'}]
l.sort(key=lambda x:x['model'])
print(l)
#l=[{'make':'Nokia','model':216,'color':'black'},{'make':'Mi Max','model':2,'color':'Gold'},{'make':'Samsung','model':7,'color':'Blue'}]
#r=sorted(l,keys=lambda x:x['model'])
#print(r)