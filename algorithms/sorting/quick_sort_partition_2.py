def fmt(ar):
    for x in ar:
        print x,
    print


def partition(ar):
    if len(ar) < 2:
        return ar
    p = ar[0]
    smaller = [x for x in ar[1:] if x < p]
    bigger = [x for x in ar[1:] if x >= p]
    return (smaller, p, bigger)

# use of recursion


def quickSort(ar):
    if len(ar) < 2:
        return ar
    (smaller, p, bigger) = partition(ar)
    res = quickSort(smaller) + [p] + quickSort(bigger)
    fmt(res)
    return res
# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
