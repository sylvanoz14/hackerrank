N = input()
ar = []
for i in xrange(0, N):
    ar.append(int((raw_input().strip().split())[0]))

count = 0
for num in xrange(0,100):
    nums = ar.count(num)
    count += nums
    print count,
