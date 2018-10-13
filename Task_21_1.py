import time
start = time.time()
#----------------- work space ------------------

def number(number):
    def num_1(num):return sum(i for i in range(1,num) if num%i == 0)
    return sum( i for i in range(2,number) if( i != num_1(i) and num_1(num_1(i)) == i))

print(number(10000))

    
#-----------------     end    ------------------
print('----------- time work ----------')
end = time.time()
print(end - start)


