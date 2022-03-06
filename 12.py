def pattern(N):
    
    for i in range(1,N+1):
        print()
        for j in range(1,i+1):
            print(j*i,end=" ")


N=int(input("Enter step number"))
pattern(N)
