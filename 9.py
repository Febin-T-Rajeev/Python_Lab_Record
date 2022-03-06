d1={8:'eight',4:'four',10:'ten',0:'zero',2:'two'}

print("The dictionary to be sorted:")
print(d1)

l1=list(d1.items())
l1.sort()
d2=dict(l1)
print("The dictionary after sorting to ascending order:")
print(d2)


l2=list(d1.items())
l2.sort(reverse=True)
d3=dict(l2)
print("The dictionary after sorting to descending order:")
print(d3)
