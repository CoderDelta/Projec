s=[]
s_sum=0
n=2
k=2
while True:
    k=2
    while k<=n**0.5:
        if n%k==0:
            n+=1
            k=2
        else:
            k+=1
    s.append(n)
    n+=1
    s_sum+=1
    if s_sum==28001:
        print(s[-1])
    
