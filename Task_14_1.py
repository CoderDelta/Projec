import time
start = time.time()
#-------------- work space ---------------
num = 1000000
dic = {1:1}
max = 0
s = []
m = []
def number(n,dic):
    if(n == 1): return 1
    elif(n%2 ==0):
        if n not in dic:
            m = dic[n] = number(n//2,dic) + 1
            return m
        else:
            m = dic[n]
            return m  
            
    else:
        if n not in dic:
            m = dic[n] =  number(n*3+1,dic)   + 1
            return m
        else:
            m = dic[n]
            return m
for n in range(1,num):
    if n not in dic:
        number(n,dic)
for k,v in dic.items():
    if k< num:
        if max < v:
            max = v
            s.append(int(k))
            m. append(int(v))
            
print(s[-1],m[-1])
#--------------     end    ---------------
print('--------- time work ---------')
end = time.time()
print(end - start)


