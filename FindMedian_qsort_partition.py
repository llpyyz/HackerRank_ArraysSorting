"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Quicksort partition fcn to find median
1/9/2015
"""
import random
import datetime

def lomutoPartition(ar, p, r):
    pivot = ar[r]
    i = p - 1
    for j in range(p, r):
        if(ar[j] <= pivot):
            i += 1
            swap(ar, i, j)
    swap(ar, i + 1, r)
    return i + 1

def swap(ar, idx1, idx2):
    tmp = ar[idx1]
    ar[idx1] = ar[idx2]
    ar[idx2] = tmp

#median of three
def choosePiv(ar, lo, hi):
    res = [ar[lo], ar[len(ar)/2], ar[hi]]
    res.sort()
    return ar.index(res[1])
    

n = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
median_idx = len(ar) / 2
lo = 0
hi = len(ar) - 1
p = choosePiv(ar,lo,hi)
swap(ar, p, hi)
done = False
while(not done):
    pividx = lomutoPartition(ar,lo,hi)
    if(pividx == median_idx):
        done = True
    elif(pividx < median_idx):
        lo = pividx + 1
    else:
        hi = pividx - 1
        
print ar[pividx]

#####

#print "\n***begin timer***\n"
#############################
bef = datetime.datetime.now()
#############################


#ub = 10000000
#lb = 0
#arr_size = 100001
#ar = [random.randint(lb,ub) for i in range(arr_size)]

median_idx = len(ar) / 2

#print "ar:",ar, "\n"
#arc = list(ar)
#arc.sort()
#print "via sort, median:", arc[len(arc)/2], "\n"
lo = 0
hi = len(ar) - 1
p = choosePiv(ar,lo,hi)
swap(ar, p, hi)
done = False
itmax = 10000
currit = 0
while(not done and currit <= itmax):
    pividx = lomutoPartition(ar,lo,hi)
    if(pividx == median_idx):
        done = True
    elif(pividx < median_idx):
        lo = pividx + 1
    else:
        hi = pividx - 1
    currit += 1
        
print ar[pividx], "\n"

#############################
aft = datetime.datetime.now()
print "et:", aft - bef
#############################
#7
#0 1 2 4 6 5 3