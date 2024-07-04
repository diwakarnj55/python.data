a=1
s=0
n=int(input("enter the number"))
for a in  range(1,n+1):
    if a%2==0:
        s=a+s
        print(a)
print("sum  :",s)