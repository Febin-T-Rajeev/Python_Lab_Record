
a=input('enter the first string')
b=input('enter the second string')
"""
x=a[0:2]
a=a.replace(a[0:2],b[0:2])
b=b.replace(b[0:2],x)
"""
a_temp=b[0:2]+a[2:]
b_temp=a[0:2]+b[2:]
a,b=a_temp,b_temp
print("After swapping")
print(a,b)
