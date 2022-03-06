file1=open('abc.txt','r')
file2=open('file.txt','w')
content=file1.readlines()
type(content)
for i in range (0,len(content)):
    if(i%2==0):
        file2.write(content[i])
    else:
        pass
file2.close()
file2=open('file.txt','r')
content1=file2.read()
print(content1)
file1.close()
file2.close()
