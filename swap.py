n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
n3=int(input("Enter number3:"))
if n1>n2 and n1>n3:
    if(n2<n3):
        temp=n1
        n1=n2
        n2=n3
        n3=temp
    else:
        temp=n1
        n1=n3
        n3=temp
elif(n2>n1 and n2>n3):
    if(n1<n3):
        temp=n2 
        n1=n3
        n3=temp
    else:
        temp=n2
        n2=n1
        n1=n3
        n3=temp
else:
    if(n1<n2):
        temp=n2
        n2=n1
        n1=temp
print(n1,n2,n3)

 
