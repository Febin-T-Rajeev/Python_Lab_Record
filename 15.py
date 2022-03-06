def factors(n):
    
    for i in range(1,n+1):
        if(n%i==0):
            print(i)


n=int(input("Enter any number"))
print("Factors of number ",n," is : ")
factors(n)
