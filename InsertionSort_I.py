"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Insertion Sort , Part I
1/6/2015
"""
def print_arr(ar):
    for elt in ar:
        print elt,
    print

def insert_elt(ar, elt):
    idx = len(ar) - 2
    while(elt < ar[idx] and idx >= 0):
        ar[idx + 1] = ar[idx]
        print_arr(ar)
        idx -= 1
    ar[idx+1] = elt
    return ar
    
def insertionSort(ar):
    if(len(ar) > 1):
        V = ar[len(ar) - 1]
        ar = insert_elt(ar, V)
    print_arr(ar)

s = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
insertionSort(ar)


##### alternate beginning:
#m = input()
#ar = [int(i) for i in raw_input().strip().split()]
#insertionSort(ar)
