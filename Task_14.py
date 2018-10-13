import time
start = time.time()

number = 10000
s = []
m = []
i = 0
for i in range(13, number):
    def number(num):
        if(num == 1): return 1
        elif(num%2 == 0): num //= 2; return number(num) + 1
        else: num = 3*num + 1; return number(num) + 1
    s.append(number(i))
    m.append(i)
print(m[s.index(max(s))])

print('--------- time work ---------')
end = time.time()
print(end - start)

