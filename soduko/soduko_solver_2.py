# My soduko version 2
# solved using backtracking
# credits to
# https://github.com/akaNiknok/sudoku-solver/blob/master/sudoku-solver.py

def is_solved(soduko):
    """ check for any emmpty spaces left """
    for row in soduko:
        if 0 in row:
            return False
    return True


def is_legal(soduko, i, j, value):
    """ check if that spot is legal for that partucal vlaue"""
    if value in soduko[i]:

        return False
    for row in soduko:
        if row[j] == value:

            return False
    top_x, top_y = 3 * (i / 3), 3 * (j / 3)

    for x in xrange(top_x, top_x + 3):
        for y in xrange(top_y, top_y + 3):
            if soduko[x][y] == value:
                return False
    return True



def solve_soduko(soduko):
    if is_solved(soduko):
        return True

    for i in xrange(0, 9):
        for j in xrange(0, 9):
            if soduko[i][j] == 0:
                for value in xrange(1, 10):

                    if is_legal(soduko, i, j, value):
                        soduko[i][j] = value

                        if solve_soduko(soduko):
                            return True

                        soduko[i][j] = 0
                return False

