a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
total=a+b+c
avg=total/3
per=total*100/300
print("sum :",total)
print("sum  :",avg)
print("sum  :",per)
if per>=80:
    print("grade a")
elif per>=60:
    print("grade b")
elif per>=40:
    print("gradec")
elif per>=20:
    print("grade d")
else:
    print("grade failed")