#will write all my tests here
# this also can not sove soduko_1
# please use soduko_solver_2 using bactracking
import timeit
from soduko_solver import *


soduko = [[5,1,7,6,0,0,0,3,4],
                [2,8,9,0,0,4,0,0,0],
                [3,4,6,2,0,5,0,9,0],
                [6,0,2,0,0,0,0,1,0],
                [0,3,8,0,0,6,0,4,7],
                [0,0,0,0,0,0,0,0,0],
                [0,9,0,0,0,0,0,7,8],
                [7,0,3,4,0,0,5,6,0],
                [0,0,0,0,0,0,0,0,0]]


soduko_1= [[0,0,5,0,6,0,7,0,0],
                [0,9,0,0,0,0,0,3,0],
                [7,0,3,0,8,0,2,0,4],
                [0,0,0,1,0,6,0,0,0],
                [6,0,7,0,0,0,4,0,3],
                [0,0,0,3,0,2,0,0,0],
                [1,0,4,0,9,0,3,0,7],
                [0,7,0,0,0,0,0,9,0],
                [0,0,8,0,3,0,1,0,0]]

start = timeit.default_timer()

solve_soduko(soduko)
for a in soduko:
    print a

stop = timeit.default_timer()

print stop - start
