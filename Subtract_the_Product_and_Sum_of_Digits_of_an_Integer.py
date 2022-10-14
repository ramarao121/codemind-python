n=int(input())
p=0
k=1
while n>0:
    s=n%10
    p=p+s
    k=k*s
    n=n//10
print(k-p)    