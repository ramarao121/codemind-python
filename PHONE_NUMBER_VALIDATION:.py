n=int(input())
a=n//1000000000
cnt=0
while n>0:
    s=n%10
    n=n//10
    cnt=cnt+1
if cnt==10:
    if a==0:
        print("Invalid")
    else:
        print("Valid")
else:
    print("Invalid")