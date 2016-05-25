
" this was so hard for me"


def partition(ar, start, end):
    pivot = end
    bigger_found = 0
    ip = 0
    for i in range(start, end):
        if ar[i] >= ar[pivot] and bigger_found < 1:
            ip = i
            bigger_found += 1
        elif ar[i] < ar[pivot] and bigger_found > 0:
            ar[i] , ar[ip] = ar[ip], ar[i]
            ip += 1
    if bigger_found > 0:
        ar[ip], ar[pivot] = ar[pivot], ar[ip]
        pivot = ip
    return pivot

def qsort(ar, start, end):
    if start < end:
        p = partition(ar, start, end)
        print ' '.join(map(str, ar))
        qsort(ar, start, p-1)
        qsort(ar, p+1, end)

