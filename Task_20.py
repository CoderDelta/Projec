import time
start = time.time()
#----------------- work space ------------------

sum = 0
def factorial(n):
    if n == 1:return 1
    else:return n*factorial(n-1)
num = str(factorial(100))
for i in range(len(num)):
    sum += int(num[i])
print(sum)

#-----------------     end    ------------------
print('----------- time work ----------')
end = time.time()
print(end - start)


