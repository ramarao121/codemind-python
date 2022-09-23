n=int(input())
count=0
for i in range(0,n):
    p=i
    if p*p==n:
        count=count+1
if count==1:
    print("True")
else:
    print("False")
    
        
