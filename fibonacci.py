n=int(input())
a=0
b=1
c=0
cnt=0
while cnt<n:
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    cnt=cnt+1