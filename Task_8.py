s1=str(73167176531330624919225119674426574742355349194934)
s2=str(96983520312774506326239578318016984801869478851843)
s3=str(85861560789112949495459501737958331952853208805511)
s4=str(12540698747158523863050715693290963295227443043557)
s5=str(66896648950445244523161731856403098711121722383113)
s6=str(62229893423380308135336276614282806444486645238749)
s7=str(30358907296290491560440772390713810515859307960866)
s8=str(70172427121883998797908792274921901699720888093776)
s9=str(65727333001053367881220235421809751254540594752243)
s10=str(52584907711670556013604839586446706324415722155397)
s11=str(53697817977846174064955149290862569321978468622482)
s12=str(83972241375657056057490261407972968652414535100474)
s13=str(82166370484403199890008895243450658541227588666881)
s14=str(16427171479924442928230863465674813919123162824586)
s15=str(17866458359124566529476545682848912883142607690042)
s16=str(242190226710556263211111093705442175069416589604080)
s17=str(7198403850962455444362981230987879927244284909188)
s18=str(845801561660979191338754992005240636899125607176060)
s19=str(5886116467109405077541002256983155200055935729725)
s20=str(71636269561882670428252483600823257530420752963450)
s=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20
s_all=[]
number=0
s_list=list(s)
for i in range(971):
    num0=1
    for k in range(i,i+13):
        num=num0*int(s_list[k])
        num0=num
    s_all.append(num)
print(max(s_all))        


