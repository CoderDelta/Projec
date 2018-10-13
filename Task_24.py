
#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                 Project Euler                    -#
#-                    Task_24                       -#
#-                                                  -#
#----------------------------------------------------#

import time

start = time.time()

#-------------------- work space ---------------------

sp = [0,1,2,3,4,5,6,7,8,9]
for k in range(1,1000000):
    i = max(i for i in range(1, len(sp)) if sp[i] > sp[i-1])
    ai =  sp[i - 1]
    l = max( l for l in range(i, len(sp)) if sp[l] > ai)
    al = sp[l]
    sp[i -1], sp[l] = al, ai
    sp = sp[0:i] + sp[i:len(sp)][::-1]
print( sp )

#-------------------    end    ---------------------
end = time.time()
print('time work - ',end - start)



