import time
start = time.time()
#----------------- work space ------------------

import calendar as cl
sum  = 0
year = 1900
while year < 2000:
    year += 1
    for moon in range(1,13):
        num = cl.monthrange(year, moon);num = num[0]
        if num == 6:sum += 1
print(sum)

 

#-----------------     end    ------------------
print('----------- time work ----------')
end = time.time()
print(end - start)


