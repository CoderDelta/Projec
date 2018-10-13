import time
start = time.time()
#-------------- work space ---------------
num  = 2**1000
num = str(num)
s = 0
for i in range(len(num)):
    s+= int(num[i:i+1])
    
print(s)
#--------------     end    ---------------
print('--------- time work ---------')
end = time.time()
print(end - start)


