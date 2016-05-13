# took me 3 days to complete. learnt alot about while loops, if statatements
# and the order of condintions in the if statement

# the code is a little long, but easy to understand for a beginer
#first find out homany levels are posible in the matrix min(m,n)/2
#for each level, extract the top, left, bottom and right corners
# find out howamany items are in this lv
#use the number of items to find out the number of times you will rotate
#rotate it and then add it to a new matrix
m,n,r = map(int, raw_input().split())
matrix = []
for _ in range(m):
    matrix.append(map(int, raw_input().split()))
new_matrix = matrix

#top
def top(matrix, lv):
    tops = []
    index = lv
    while index < n-lv:
        M,N = lv, index
        value = matrix[M][N]
        tops.append([value,M,N])
        index +=1
    return tops
#left sides
# try to guard against a value not being there
def left(matrix, lv):
    lefts = []
    index = lv+1
    while index < (m -1-lv):
        M = index
        N = lv
        value = matrix[M][N]
        lefts.append([value,M,N])
        index += 1
    return lefts
#bottom
# try to optimize with (m-lv)
def bottom (matrix, lv):
    bottoms =[]
    index = lv
    while index < n-lv :
        M,N = m-lv-1 , index
        value =  matrix[M][N]
        bottoms.append([value,M,N])
        index += 1
    return bottoms
#right
def right (matrix, lv):
    rights =[]
    index = lv + 1
    while index < (m-1-lv):
        M,N = index, n-lv-1
        value = matrix[M][N]
        rights.append([value,M,N])
        index += 1
    return rights

def shift (side, rounds, lv, m, n):
    if len(side) > 0:
        for pair in side:
            index = rounds
            value = pair[0]
            M = pair[1]
            N = pair[2]
            c_ms = m-lv -1
            c_ns = n-lv -1
            while index > 0:
                # is_top, move left
                if index > 0 and (M == lv) and ( N > lv):
                    #print "top ran"
                    N -= 1
                    index -= 1
                # is_left, move down
                if index > 0 and M < c_ms  and N == lv: # cms_
                    #print "left ran"
                    M += 1
                    index -= 1
                # is_right, move up
                if index > 0 and M > lv and N == c_ns: # cns
                    #print " right ran"
                    M -= 1
                    index -= 1
                #is_bottom, move up
                if index > 0 and M == c_ms  and N < c_ns : #cms & cns
                    #print "bottom ran"
                    N += 1
                    index -= 1
            new_matrix[M][N] = value

def rotate(matrix, m, n, r):
    lvs  = int(min(m,n) / 2)
    for lv in range(lvs):
        tops = top(matrix, lv)
        lefts = left(matrix, lv)
        bottoms = bottom(matrix, lv)
        rights = right(matrix, lv)
        sums =   len(lefts)+ len(rights)+ len(tops)+ len(bottoms) # take 4 out
        rounds = r % sums
        shift(tops,rounds, lv, m, n)
        shift(lefts,rounds, lv, m, n)
        shift(bottoms,rounds, lv, m, n)
        shift(rights,rounds, lv, m, n)

    return new_matrix


for c in rotate(matrix, m, n, r):
        print ' '.join(map(str, c))
