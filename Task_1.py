a=(list(range(1,1000,1)))
k=0
for i  in a:
    if i%3==0 or i%5==0:
        i=k+i
        k=i       
print(i)        
        

