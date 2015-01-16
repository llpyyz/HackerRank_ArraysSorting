"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Insertion Sort , Part I
(Full insertion sort)
1/6/2015
"""
def print_arr(ar):
    for elt in ar:
        print elt,
    print

def insert_elt(ar, elt, elt_idx):
    idx = elt_idx - 1
    while(idx >= 0 and elt < ar[idx]):
        ar[idx + 1] = ar[idx]
        #print_arr(ar)
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
        print_arr(ar)
        idx += 1

s = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
insertionSort(ar)

###

"""
This version counts the number of shifts
which grows quadratically with n in the worst 
case scenario (array is sorted in reverse order initially)
"""
def insertion_sort(l):
    shifts = 0
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           shifts += 1
           j -= 1
        l[j+1] = key
    print shifts

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
