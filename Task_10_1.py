import time
start = time.time()
number = 2000000
a=0
#s = [1 for i in range(2, number + 1)]
s=[1]*(number-1)
for n in range(2,len(s)):
    if s[n]==1:
        a+=n
        i=n
        max=len(s)/n
        while i<max:
            s[n*i]=0
            i+=1
print(a)

print('--------- time work---------')
end = time.time()

print(end - start)
