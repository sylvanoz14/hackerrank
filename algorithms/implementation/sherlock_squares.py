# my original way. this will work well for small numbers but will run out of memory for large numbers
import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input().strip()
    b =n.split()
    count = 0
    for x in range(465868129, 988379794):#(int(b[0]),int(b[1]) + 1):

        x_root = int(x ** 0.50)
        x_root_sq = x_root ** 2
        if x == x_root_sq:
            count += 1
    print count

#after reading some comments, a better way to look at the problem is to
# find the square root of the min value and max value and count all the numbers inbetween. :)

import math
T = int(raw_input())
for i in xrange(T):
    l,u = map(int, raw_input().split(' '))
    count = 0
    ls = int(math.sqrt(l))
    us = int(math.sqrt(u))
    for i in xrange(ls,us):
        count +=1
    if ls*ls ==l:
        count+=1
    print count

