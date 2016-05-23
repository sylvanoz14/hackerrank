# try to build a soduko solver which mimics how i solve soduko

# requirements, min 16 numbers should be provided
# any number that is not given is assigned an original value of 0

# soduko made of 9 rows and 9 columns

"""soduko = [[_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
                 [_,_,_,_,_,_,_,_,_],
]
"""
# count all rezo's at the start of the program
def zero_count(soduko):
    zero_counts = 0
    for row in soduko:
        zero_counts += row.count(0)
    return zero_counts

# a soduko can only be solved if there are 16 or more numbers
def has_min_zero(zero_counts):
    if zero_counts > 65: # 81 - 16
        return False
    else:
        return True

# check at the begining if the soduko is already solved
def is_solved(zero_counts):
    if zero_counts == 0:
        return True
    else:
        return False

# keep updating zero_counts if any value is found
# guard against going to negative trritory
def update_zero_counts(zero_counts):
    if zero_counts == 0:
        print "something went wrong with update_zero_counts"
    zero_counts -= 1
    return zero_counts

# boxes are grids of 9 values
def box_values(soduko):
    box1, box2, box3, box4, box5, box6, box7, box8, box9 = [],[],[],[],[],[],[],[],[]
    for row in xrange(0, len(soduko)):
        if row in [0,1,2]:
            for j in xrange(0, len(soduko)):
                if j in [0,1,2]:
                    box1.append(soduko[row][j])
                if j in [3,4,5]:
                    box2.append(soduko[row][j])
                if j in [6,7,8]:
                    box3.append(soduko[row][j])
    if row in [3,4,5]:
            for j in xrange(0, len(soduko)):
                if j in [0,1,2]:
                    box4.append(soduko[row][j])
                if j in [3,4,5]:
                    box5.append(soduko[row][j])
                if j in [6,7,8]:
                    box6.append(soduko[row][j])
    if row in [6,7,8]:
            for j in xrange(0, len(soduko)):
                if j in [0,1,2]:
                    box7.append(soduko[row][j])
                if j in [3,4,5]:
                    box8.append(soduko[row][j])
                if j in [6,7,8]:
                    box9.append(soduko[row][j])
    return box1, box2, box3, box4, box5, box6, box7, box8, box9

#update box_values -- everytime a value is found

def update_box(box, found):
    if found not in box and 0 in box:
        box.remove(0)
        box.append(found)
    else:
        print " box alreday contain number or no zeros left`"


def which_box(row,j, found):
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











