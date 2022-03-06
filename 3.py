string=input("enter a string")
words=string.split()
d={}
for w in words:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
for x in d.keys():
    print("%s occures%s times"%(x,d[x]))
