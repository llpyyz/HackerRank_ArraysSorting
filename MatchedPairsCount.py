"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Counting matched pairs via count sort
1/9/2015
"""
def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod

def npr(n, r):
    """
    Calculate the number of ordered permutations of r items taken from a
    population of size n.

    >>> npr(3, 2)
    6
    >>> npr(100, 20)
    1303995018204712451095685346159820800000
    """
    assert 0 <= r <= n
    return product(range(n - r + 1, n + 1))

def count_occurences(ar, lb = 0, ub = 99):
    counts = [0 for i in range(lb , ub + 1)]
    for elt in ar:
        counts[elt-lb] += 1
    return counts

T = input()
for i in range(T):
    N = input()
    ar = raw_input()
    ar = ar.split(' ')
    ar = [int(x) for x in ar]
    c = count_occurences(ar, 1, 10**6)
    print sum([npr(n,2) for n in c if n > 1])



#bef = datetime.datetime.now()        
#
#ub = 1
#lb = 10
#num = 100000
#l = [random.randint(ub,lb) for i in range(num)]
##print l,"\n"
#c = count_occurences(l,ub,lb)
#print c, "\n"
#print sum([npr(n,2) for n in c if n > 1]), "\n"
#
#
#aft = datetime.datetime.now()    
#print "et:", aft - bef