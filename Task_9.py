def number():
    i=1
    for a in range(i,1000):
        for b in range(a+1,1000):
            for c in range(b+1,1000):
                if a**2+b**2==c**2:
                    if a+b+c==1000:
                        return (a*b*c,a,b,c)
    i=+1
print(number())
