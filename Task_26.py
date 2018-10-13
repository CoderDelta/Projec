
#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                 Project Euler                    -#
#-                    Task_26                       -#
#-                                                  -#
#----------------------------------------------------#

import time

start = time.time()

#-------------------- work space ---------------------

def num(n):
    l = 0
    r = 1
    while l != n + 1:
        r = (10*r)%n
        l += 1
    c = r
    r = (10*r)%n
    k = 1
    while r != c:
        r = (10*r)%n
        k += 1
    return(k)
print(max([[num(n),n] for n in range(1,1000)])[1])
#-------------------    end    ---------------------
end = time.time()
print('time work - ',end - start)



