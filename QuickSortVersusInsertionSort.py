"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Quicksort vs. Insertion Sort
Counting swaps versus shifts
1/7/2015
"""

#####################
##### Quicksort #####
#####################
def quickSort2(ar, lo, hi):
    if lo < hi:
        p = lomutoPartition(ar, lo, hi)
        #p = partition2(ar, lo, hi)
        quickSort2(ar, lo, p - 1)
        quickSort2(ar, p + 1, hi)

#def partition2(ar, lo, hi):
#    
#    piv_idx = choosePiv(ar, lo, hi)
#    piv_val = ar[piv_idx]
#    swap(ar , piv_idx , hi)
#    tmp_idx = lo
#    for i in range(lo, hi):
#        if(ar[i] < piv_val):
#            swap(ar, i, tmp_idx)
#            
#            tmp_idx += 1
#    swap(ar, tmp_idx, hi)
#    
#    
#    #print ' '.join(map(str,ar))
#    return tmp_idx
    
def lomutoPartition(ar, p, r):
    pivot = ar[r]
    i = p - 1
    for j in range(p, r):
        if(ar[j] <= pivot):
            i += 1
            swap(ar, i, j)
    swap(ar, i + 1, r)
    return i + 1

def choosePiv(ar, lo, hi):
    return lo
    
def swap(ar, idx1, idx2):
    global swap_count
    swap_count += 1
    tmp = ar[idx1]
    ar[idx1] = ar[idx2]
    ar[idx2] = tmp

#####################
### end quicksort ###
#####################

######################
### insertion sort ###
######################

#def print_arr(ar):
#    for elt in ar:
#        print elt,
#    print

def insert_elt(ar, elt, elt_idx):
    global shift_count
    idx = elt_idx - 1
    while(idx >= 0 and elt < ar[idx]):
        ar[idx + 1] = ar[idx]
        shift_count += 1
        idx -= 1
    ar[idx+1] = elt
    return ar
    
def insertionSort(ar):
    if(len(ar) == 1):
        idx = 0
    else:
        idx = 1
    while(idx < len(ar)):
        V = ar[idx]
        ar = insert_elt(ar, V, idx)
        idx += 1

### end insertion sort ###

shift_count = 0
swap_count = 0

s = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
if(len(ar) == 1):
    print 0
else:
    quickSort2(list(ar), 0, len(ar) - 1)
    insertionSort(list(ar))
    print shift_count - swap_count
