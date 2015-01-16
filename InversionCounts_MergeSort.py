"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Inversion Counting (Merge Sort)
1/8/2015
"""
import datetime
import random


def mergeSort(lst, c):
    if len(lst) < 2:
        return lst
    m = len(lst) / 2
    return merge(mergeSort(lst[:m], c), mergeSort(lst[m:], c), c)
    
      
def merge(l, r, c):
    res = []
#    print "*****Begin merge*****\n"
#    print "left:",l, "right:", r, "count",c, "\n"
    while(l and r):
        if(l[0] <= r[0]):
            s = l
#            print "s == l"
        else:
            s = r
#            print "s == r"
        res.append(s.pop(0))
#        print "res:", res, "; l", l, "; r", r, "; s", s,"\n"
        if(s == r and not s == l):
            c[0] += len(l)
#            print "inversions detected:", len(l), "ic:", c, "\n"
            
    res.extend(l if l else r)
#    print "after while loop, res:", res, "count",c
#    print "*****End merge*****\n"
    return res

bef = datetime.datetime.now()

s1 = ''
ar = s1.split(' ')
ar = [int(t) for t in ar]
count = [0]
r =  mergeSort(ar, count)
print count[0]


aft = datetime.datetime.now()
print "et1:", aft - bef, "\n"


#test case 9 
#input sizes:
#95059
#44582
#35098
#34935
#33588

#output:
#2265950446 - correct
#497748006 - correct
#308181681 - correct
#304640321 - off by 1?
#281778295 - off by 1?

#ar = [1,8,8,8,2,7,1,7,4,1,2,1,1,4,8,1,2]
#ar = [random.randint(1,100) for i in range(100000)]
#ar = [1,1,1,2,2,2,2,3,4,6,8,8,9]

#print sum([ar[i] > ar[j] and i < j for i in range(len(ar)) for j in range(len(ar))])