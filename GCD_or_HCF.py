n,m=map(int,input().split())
a=max(n,m)
while True:
    if n%a==0 and m%a==0:
        print(a)
        break
    a=a-1