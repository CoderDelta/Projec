def num():
    i=0
    while True:
        i+=1
        num0=0
        for k in range(1,21):
            if i%k==0:
                num0+=1
                if num0==20:
                    return i
                else:
                    continue
print(num())                 
