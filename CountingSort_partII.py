"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Counting Sort II
1/8/2015
"""

def count_occurences(ar, lb = 0, ub = 99):
    counts = [0 for i in range(lb , ub + 1)]
    for elt in ar:
        counts[elt] += 1
    return counts

n = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
lo = 0
hi = 99
c = count_occurences(ar, lo, hi)
print ' '.join([' '.join(map(str, c[i]*[i])) for i in range(len(c)) if c[i] > 0])

