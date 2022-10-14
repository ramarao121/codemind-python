n=int(input())
t=n
s=0
while n>0:
    p=n%10
    s=s*10+p
    n=n//10
if t==s:
    print("True")
else:
    print("False")
