"""
David Schonberger
Hackerrank.com
Arrays and Sorting - In-place quicksort
1/6/2015
"""

def quickSort2(ar, lo, hi):
    if lo < hi:
        p = partition2(ar, lo, hi)
        quickSort2(ar, lo, p - 1)
        quickSort2(ar, p + 1, hi)
        
def partition2(ar, lo, hi):
    piv_idx = choosePiv(ar, lo, hi)
    piv_val = ar[piv_idx]
    swap(ar , piv_idx , hi)
    tmp_idx = lo
    for i in range(lo, hi):
        if(ar[i] < piv_val):
            swap(ar, i, tmp_idx)
            tmp_idx += 1
    swap(ar, tmp_idx, hi)
    
    print ' '.join(map(str,ar))
    return tmp_idx
    
def choosePiv(ar, lo, hi):
    return hi
    
def swap(ar, idx1, idx2):
    tmp = ar[idx1]
    ar[idx1] = ar[idx2]
    ar[idx2] = tmp
    

s = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
if(len(ar) == 1):
    print ar[0]
else:
    quickSort2(ar, 0, len(ar) - 1)
