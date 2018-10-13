import time
start = time.time()
#-------------- work space ---------------


d1 = {'one':3,'two':3,'three':5,'four':4,'five':4,'six':3,'seven':5,
      'eight':5,'nine':4}
d2 = {'ten':3,'eleven':6,'twelve ':6,'thirteen':8, 'fourteen':8,'fifteen':7,
      'sixteen':7,'seventeen':9,
      'eighteen':8,'nineteen':8}
d3 = {'twenty':6,'thirty':6,'forty':5,'fifty':5,'sixty':5,'seventy':7,
      'eighty':6,'ninety':6}
m = 0 
def one(d1,d2):
    for k,v in d1.items():d2.update({k:v});
    return d2
def twenty(d1,d2,d3):
    for  k,v in d3.items():
        d2.update({k:v})
        for i,n in d1.items():d2.update({k + i:v + n})
    return d2
def hundred(d1,d2,d3):
    for k,v in d1.items():
        d2.update({k + 'hundred':v + 7})
        for i,n in d3.items():d2.update({k + 'hundred' + 'and' + i:v + n + 10})
    d2.update({'onethousand':11});return d2
d6 = hundred(d1,d2,twenty(d1,one(d1,d2),d3).copy()).copy()
for k,v in d6.items():
    m += v
print(m)
    

    
#--------------     end    ---------------
print('--------- time work ---------')
end = time.time()
print(end - start)


