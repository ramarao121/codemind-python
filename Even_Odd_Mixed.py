n=int(input())
cnt=0
snt=0
while n>0:
    s=n%10
    n=n//10
    if s%2==0:
        cnt=cnt+1
    else:
        snt=snt+1
if snt==0:
    print("Even")
if cnt==0:
    print("Odd")
if snt>0 and cnt>0:
    print("Mixed")