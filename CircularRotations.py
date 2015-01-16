"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Circular rotations (Not a sorting problem)
1/9/2015
"""
#return ar with rightmost n elts moved to front
def rc_rotate_arr(ar, n):
    for i in range(n):
        ar.insert(0, ar.pop())
    return ar

line1 = raw_input()
line1 = line1.split(' ')
N = int(line1[0])
K = int(line1[1])
Q = int(line1[2])

ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
ar = rc_rotate_arr(ar,K)

for i in range(Q):
    print ar[input()]
    
