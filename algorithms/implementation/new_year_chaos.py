#!/bin/python
# continuing on my quest to learn.
# learnt about bubble sorting algorithm and optimization.
# a normal bubble algorithm will fail this test, but by watching this video,
# https://www.youtube.com/watch?v=Yaj07QdVTp8,
# I was able to optimize and cut out extra work.

import sys
def sort (q,n):
    moved = {}
    for a in q:
        moved[a] = 0
    last = n-1
    swapped = False#optimize

    for i in xrange(0,last ):
        for j in xrange(0,last):
            if q[j] > q[j+1]:
                if moved[q[j]] >= 2 :
                    return "Too chaotic"
                moved[q[j]] += 1
                temp = q[j]
                q[j] = q[j+1]
                q[j+1] = temp
                swapped = True
        if swapped:#optimze
            swapped = False
        else:
            break
        last -= 1#optimize

    sum_ = 0
    for item in moved:
        sum_ += moved[item]

    return sum_



T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    # your code goes here
    print sort(q,n)
