def Fibonacci(m):
    f0=0
    f1=1
    s0=0
    while True:
        f=f0+f1
        sum_f=f
        f0=f1
        f1=f
        if sum_f%2==0:
            if sum_f<4000000:
                s=sum_f+s0
                s0=s
                if sum_f>4000000:
                    s=s-sum_f
                    break
            elif sum_f>4000000:
                 break
    return s
print(Fibonacci(0))
