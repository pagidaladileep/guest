r=int(input("Enter number range:"))
a=0
b=1
c=1
print(a,b,end="")
while((a+b)<r):
    c=a+b
    a=b
    b=c
    print(c,end="")
