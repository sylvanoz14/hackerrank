import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    
    chocolates = n // c # chocolate got with money
    total_wrappers = chocolates # total wrappers
    
    while total_wrappers >= m: #while you have more chocolates than wrappers
        total_wrappers -= m  # remove wrappers handed to store
        total_wrappers += 1 # include wrapper from "incentive" chocolate
        chocolates += 1 # add 1 chocolate to total chocalte eaten
    print chocolates
 
