s_list=[]
def palinom():
    for i in range(100,1000):
        k=1000
        while k>=100:
            s=str(i*k)
            s0=s[::-1]
            k-=1
            if s0==s:
                s_list.append(int(s))
    return s_list
a=palinom()
print(max(a))

