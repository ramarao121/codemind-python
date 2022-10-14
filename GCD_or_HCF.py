n,m=map(int,input().split())
s=max(n,m)
while "True":
    if n%s==0 and m%s==0:
        print(s)
        break 
    s=s-1