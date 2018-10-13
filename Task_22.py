import time
start = time.time()
#----------------- work space ------------------

dic = {}; sp = []; sum = 0; sum_1 = 0; byk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(byk)): dic[byk[i]] = i+1
f = open('mark', mode = 'r')
ls = f.read();st = ''; num = 0; list = []
for index in range(len(ls)):
    if ls[index] == '"':
        num += 1
        if num == 2:  list.append(st); st = '';num = 0
    elif ls[index] == ',': continue            
    else:st += ls[index]
ls = sorted(list)
for k in range(len(ls)):
    for q in range(len(ls[k])): sum += dic[ls[k][q]]
    n = sum*(k + 1); sp.append(int(n)); sum = 0
for m in sp: sum_1 += m
print(sum_1)
    
#-----------------     end    ------------------
print('----------- time work ----------')
end = time.time()
print(end - start)


