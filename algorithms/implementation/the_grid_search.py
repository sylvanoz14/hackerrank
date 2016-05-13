# my approach is to devide and serch
#small grids of r rows. then i loop
# via those small grids trying to find patterns

#slice
# slice the big grid into small grids
# make sure the sliced-list conatains no more or no less than r rows

#pattern_in_slice
# try to match pattern within the small grid
# take into account a part of the pattern may occur multiple times in a line
# while there is still an occurence
# find subsequent pattern items at same location on row below

#solve
# do the above process until you find a match, if
# no match is found, return NO


#!/bin/python

import sys


def slice (G, R, r, start):
    sliced_G = []
    end = start + r
    if end > (R):
        return sliced_G
    else:
        sliced_G = G[start: end]
        return sliced_G

def pattern_in_slice (sliced_G, P):
    if P[0] in sliced_G[0]:
        start = 0
        while  sliced_G[0].find(P[0], start) != -1 :
            position = sliced_G[0].find(P[0], start)
            index = 1
            true = 1
            while index < len(sliced_G):
                if P[index ] in sliced_G[index] and sliced_G[index].find(P[index], start) == position :
                    true += 1
                index += 1
            if true == len(sliced_G):
                return True
            start = position + 1
    return False


def solve(G,R,P,r):
    start = 0
    for start in range (0, len(G)):
        sliced_G = slice (G, R, r, start)
        if len(sliced_G) != 0:
            if pattern_in_slice (sliced_G, P):
                return "YES"
    return "NO"


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    print solve(G,R,P,r)
