def number():
    a=2000001
    m=2
    s=[2]
    n=3
    i=1
    while n <=a: 
        while i<=len(s):
            if n%s[i-1]==0:
                n+=2
                if n>=a:
                    return sum
                i=1
            i+=1
        sum=m+n
        m=sum
        if n**2<=a:
            s.append(n)
            i=1
        n+=2
        i=1
    return sum
print(number())
