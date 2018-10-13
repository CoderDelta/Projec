class number():
    def sum_kv(self):
        num0=0
        for i in range(1,101):
            num=num0+i**2
            num0=num
        return num

    def kv_sum(self):
        num1=0
        for k in range(1,101):
            num2=num1+k
            num1=num2
        return num2**2
a=number()
print(a.kv_sum()-a.sum_kv())

