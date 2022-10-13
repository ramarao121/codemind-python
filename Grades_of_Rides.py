p,k,b=map(int,input().split())
if p>50 and k>60 and b>100:
    print(10)
elif p>50 and k>60:
    print(9)
elif k>60 and b>100:
    print(8)
elif p>50 and b>100:
    print(7)
elif p>50 or k>60 or b>100:
    print(6)
if p<=50 and k<=60 and b<=100:    
    print(5)