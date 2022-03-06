def list_reven(l):

    l2=[]

    for i in l:
        if(i%2!=0):
            l2.append(i)

    return l2



n=input("Enter integers space separated")
list1=list(map(int,n.split()))
print("list before removing even integers: ",list1)
list2=list_reven(list1)
print("list after removing even integers: ",list2)


           
