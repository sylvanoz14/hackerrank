N = input()
lst = [int(x) for x in raw_input().strip().split(' ')]

max_ = max(lst)
for x in xrange(0, max_ + 1):
    print lst.count(x),

