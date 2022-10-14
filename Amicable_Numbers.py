n=int(input())
m=int(input())
s=0
p=0
for i in range(n-1,0,-1):
    if n%i==0:
        s=s+i
for j in range(m-1,0,-1):
    if m%j==0:
        p=p+j
if p==n and s==m:
    print("Amicable")
else:
    print("Not Amicable")
    