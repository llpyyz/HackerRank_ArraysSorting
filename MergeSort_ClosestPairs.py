"""
David Schonberger
Hackerrank.com
Arrays and Sorting - Merge sort - Finding closest pairs
1/9/2015
"""
def mergeSort(lst, c):
    if len(lst) < 2:
        return lst
    m = len(lst) / 2
    return merge(mergeSort(lst[:m], c), mergeSort(lst[m:], c), c)

def merge(l, r, c):
    res = []
    while(l and r):
        if(l[0] <= r[0]):
            s = l
        else:
            s = r
        res.append(s.pop(0))
        if(s == r and not s == l):
            c[0] += len(l)
            
    res.extend(l if l else r)
    return res

n = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
count = [0]
srted = mergeSort(ar,count)
min_diff = min([srted[i+1] - srted[i] for i in range(0,len(srted) - 1)])
print ' '.join([' '.join(map(str,[srted[i], srted[i+1]])) for i in range(0, len(srted) - 1) if srted[i+1] - srted[i] == min_diff])

###
def permute(lst):
    for i in range(len(lst)):
        idx = random.randint(0,len(lst) - 1)
        tmp = lst[i]
        lst[i] = lst[idx]
        lst[idx] = tmp
        

lb = -2000
ub = -lb + 1
rng = range(lb,ub)
#print rng, "\n"
remove = int(4 * ub)
remove_idx = []
for i in range(remove):
    remove_idx.append(random.randint(lb, ub))

remove_idx = list(set(remove_idx))
#print remove_idx, "\n"
#print len(remove_idx), "\n"

rng = [elt for elt in rng if not elt in remove_idx]
#print rng, "\n"

permute(rng)
#print rng, "\n"

print "len of lst", len(rng)
print "\n***begin timer***\n"
#############################
bef = datetime.datetime.now()
#############################


count = [0]
srted = mergeSort(rng,count)
#print srted, "\n"
#diffs = [srted[i+1] - srted[i] for i in range(0,len(srted) - 1)]
#print diffs, "\n"
min_diff = min([srted[i+1] - srted[i] for i in range(0,len(srted) - 1)])
#print min_diff, "\n"
print ' '.join([' '.join(map(str,[srted[i], srted[i+1]])) for i in range(0, len(srted) - 1) if srted[i+1] - srted[i] == min_diff])
#print min_diff_pairs


#############################
aft = datetime.datetime.now()
print "et:", aft - bef
#############################