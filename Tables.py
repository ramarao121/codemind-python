n,r=map(int,input().split())
for i in range(n,n+1):
    for j in range(1,r+1,2):
        print(i,"x",j,"=",i*j)