a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    cnt=0
    while n>0:
        p=n%10
        if p>0:
            if i%p==0:
                cnt=cnt+1
        n=n//10
    if len(str(i))==cnt:
        print(i,end=" ")
            
    

    
    