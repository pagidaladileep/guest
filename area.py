n=int(input("Enter choice 1-triangle 2-rectangle 3-square"))
b=int(input("Enter base:"))
if(n==1):
    h=int(input("Enter height :"))
    a1=0.5*b*h
    print(a1)
elif(n==2):
    l=int(input("Enter length"))
    a2=l*b
    print(a2)
else:
    s=int(input("Enter side"))
    a3=s*s;
    print(a3)
