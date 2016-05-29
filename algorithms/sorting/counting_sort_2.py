N = input()
lst = [int(x) for x in raw_input().strip().split(' ')]

max_ = max(lst)
for x in xrange(0, max_ + 1):
    count_ =  lst.count(x)
    for _ in xrange(0,count_):
        print x,
