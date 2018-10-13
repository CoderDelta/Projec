
#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                 Project Euler                    -#
#-                    Task_23                       -#
#-                                                  -#
#----------------------------------------------------#

import time
import itertools

start = time.time()

#-------------------- work space ---------------------

numb = 28124


def simpel(num):
    n = 1
    i = 0
    while n*n <= num:
        if num%n == 0:
            n += 1
            i += 1
        else:
            n +=1
    if i > 2:
        return 'True'
    
sp = { i  for i in  range(1,numb)  if simpel(i) == 'True' }

def number(num):
    k = num
    i = 2
    suma = 1    
    mul = 1
    n = 1
    while num > 1:
        if num%i == 0:
            num = num//i
            suma += i*n
            n *= i
        else:
            i += 1
            mul *= suma
            n = 1
            suma = 1          
    mul *= suma
    mul = mul - k
    return mul
   
sq=set([])
sl = { i for i in sp if number(i) > i }
sk = { i  for i in  range(1,numb) }

for i in sl:
   for k in sl:
      sq.add(i + k)
   
num =sk-sq
print(sum(num))




#-------------------    end    ---------------------
end = time.time()
print('time work - ',end - start)



