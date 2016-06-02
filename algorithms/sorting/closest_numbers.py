# line 4 KEY. sorting the original list makes the algo linear

N = input()
lst = [int(x) for x in raw_input().strip().split(' ')]

lst.sort()
min_ = 0
min_list = []
first = True

for i in xrange(1, N):
    if lst[i - 1] == lst[i]:
        continue
    new_min = abs(lst[i] - lst[i - 1])
    if first:
        min_ = new_min
        min_list = [lst[i - 1], lst[i]]
        first = False
    else:
        if new_min > min_:
            continue
        elif new_min == min_:
            min_list.extend((lst[i -1], lst[i]))
        else:
            min_ = new_min
            min_list = [lst[i -1], lst[i]]

print ' '.join(map(str,min_list))
