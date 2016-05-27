def quick_sort(lst, left, right):
    if left >= right:
        return 0
    lp = rp = left
    pivot = lst[right]
    count = 1
    while rp < right:
        if lst[rp] < pivot:
            lst[rp],lst[lp] = lst[lp],lst[rp]
            lp += 1
            count += 1
        rp += 1
    lst[lp],lst[right] = lst[right],lst[lp]

    count += quick_sort(lst, left, lp-1)
    count += quick_sort(lst, lp+1, right)
    return count

def insert_sort(lst):
    lst_len = len(lst)
    count = 0
    for i in xrange(lst_len):
        for j in xrange(i+1, lst_len):
            if lst[i] > lst[j]:
                count += 1
    return count

N = input()
lst = [int(x) for x in raw_input().strip().split(' ')]
print insert_sort(lst) - quick_sort(lst, 0, len(lst)-1)
