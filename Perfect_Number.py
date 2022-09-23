n=int(input())
s=0
for i in range(n-1,0,-1):
    if n%i==0:
        s=s+i
if s==n:
    print("True")
else:
    print("False")