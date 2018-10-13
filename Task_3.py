def nuber_simpel(num):
    i=2
    while num>1:
        if num%i==0:
            num=int(num/i)
        else:
            i+=1
    return i
print(nuber_simpel(600851475143))

