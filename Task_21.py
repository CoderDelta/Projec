import time
start = time.time()
#----------------- work space ------------------

ls = [ i for i in range(2,10000)];summer = 0

def num_1(num):return sum(i for i in range(1,num) if num%i == 0)

for num in ls:
    sum_1 = num_1(num)
    sum_2 = num_1(sum_1)
    if sum_1 == num:continue
    else:
        if num == sum_2:
            ls.remove(sum_1)
            summer_1 =summer + num + sum_1
            summer = summer_1
print(summer_1)

    
#-----------------     end    ------------------
print('----------- time work ----------')
end = time.time()
print(end - start)


