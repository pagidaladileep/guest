num=int(input("Enter number"))
sum=0;
temp=num;
while num>0:
    rem=num%10
    sum=sum+rem*rem*rem
    num=num//10
if(temp==sum):
    print("sum is armstrong" )
else:
    print("sum is not armstrong")