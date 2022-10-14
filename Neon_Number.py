n=int(input())
a=n*n
s=0
while a>0:
    p=a%10
    s=s+p
    a=a//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")