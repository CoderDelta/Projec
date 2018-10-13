import time
start = time.time()
#-------------- work space ---------------

f = open('graf', mode = 'r')
s = [];m = []
for line in f:
    if line[0] == '0':line ='0'+str(int(line))
    else:line =str(int(line))       
    for i in range(0,len(line)-1,2):m.append(int(line[i:i+2]))
    s.append(m);m = []
s_inv = []
for  n in range(len(s)):s_inv.append(s[-(1+n)])
s = s_inv
for j in range(1,len(s)):
    for i in range(len(s[j])):s[j][i] = s[j][i] + max(s[j - 1][i],s[j - 1][i + 1])
print(s[-1][-1])
    
    
#--------------     end    ---------------
print('--------- time work ---------')
end = time.time()
print(end - start)


