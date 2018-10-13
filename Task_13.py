import time
start = time.time()

f=open('my_file', mode='r')
s=[];sum = 0
for line in f:s.append(int(line))
for k in range(len(s)):sum += s[k]
f.close()
print(str(sum)[:10])

print('--------- time work---------')
end = time.time()
print(end - start)

    
        
