
#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                 Project Euler                    -#
#-                    Task_25                       -#
#-                                                  -#
#----------------------------------------------------#

import time

start = time.time()

#-------------------- work space ---------------------
# знайдо числа фибоначи

n  = 3
bf = 1
af = 1
while True:
    fib = bf + af
    bf = af
    af = fib 
    if len(str(fib))== 1000:
        print(n)
        break
    n += 1

    


#-------------------    end    ---------------------
end = time.time()
print('time work - ',end - start)



