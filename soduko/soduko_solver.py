# the solve_soduko first calls fill boxes, which firsts empties all the boxes and then refills them
# then it starts looking from the top right corner for any "0". 0 means that space is unfield.
# when it finds one, it starts trying for valid numbers using the is_not_in_any function.
# is_not_in_any returns true if the value you are trying (try_) is not any colum, row or box associated with than space
# if the length of possibles is 1, meaning only one possible value, we place that vlue in that space, else we just find the next one.
# after trying all the boxes, if there is still a zero within the soduko, we cal solve_soduko again otherwise we return the solved soduko

# this solution may work well for easy soduko, but may get stucked with more difficult soduko.
# the solution can be improved by getting rid og 9 boxes (lists are expensive)
# i will try implementing a version two using backtracking
# hope u enjoy it
# Test is found in soduko_solver_tests.py

box1, box2, box3, box4, box5, box6, box7, box8, box9 = [],[],[],[],[],[],[],[],[]


# update box_values -- everytime a value is found

def update_box(box, found):
    if found not in box and 0 in box:
        box.remove(0)
        box.append(found)
    else:
        print " box alreday contain number or no zeros left`"

def which_box(row, j):
    if row in [0,1,2]:
            if j in [0,1,2]:
                return box1
            if j in [3,4,5]:
                return box2
            if j in [6,7,8]:
                return box3
    if row in [3,4,5]:
            if j in [0,1,2]:
                return box4
            if j in [3,4,5]:
                return box5
            if j in [6,7,8]:
                return box6
    if row in [6,7,8]:
            if j in [0,1,2]:
                return box7
            if j in [3,4,5]:
                return box8
            if j in [6,7,8]:
                return box9

def fill_boxes(soduko):
    box1, box2, box3, box4, box5, box6, box7, box8, box9 = [],[],[],[],[],[],[],[],[]
    for row in xrange(0, 9):
        for j in xrange(0, 9):
            which_box(row, j).append(soduko[row][j])

def is_not_in_any(row, j, try_, box, soduko):
    # check row
    if  try_ in soduko[row]:
        return False
    for i in xrange(0, 9):
        # check col
        if try_ == soduko[i][j]:
            return False
    if try_ in box:
        return False
    return True



def solve_soduko(soduko):

    fill_boxes(soduko)
    for row in xrange(0,9):
        for j in xrange(0,9):
            if soduko[row][j] ==0:
                # try incerting numbers
                possible = []
                for try_ in xrange(1,10):
                    if is_not_in_any(row, j, try_, which_box(row, j), soduko):
                        possible.append(try_)
                if len(possible) == 1:
                    soduko[row][j] = possible[0]
                    update_box(which_box(row, j), possible[0])
    for row in soduko:
        if 0 in row:
            solve_soduko(soduko)
        else:
            return soduko






