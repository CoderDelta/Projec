import time
start = time.time()
n = 3
while True:
    n+= 1;number = 0.5*n*(n+1);number_0 = number;i = 2;s = []
    while i <= number:
        if(number%i == 0):number = number/i;s.append(i)
        else:i+= 1    
    def num(k):
        number = 0
        for i in range(k,len(s)):
            if(s[i] == s[k]):   
                number+= 1
                if(i == len(s)-1):return number + 1
            else:return num(i)*(number + 1)
    if num(0) >= 500:print(int(number_0));break
print('--------- time work---------')
end = time.time()
print(end - start)
