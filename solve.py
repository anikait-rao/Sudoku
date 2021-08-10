'''
solve.py

This module solves any Sudoku board using the backtracking algorithm!
'''

def solve(grid, i = 0, j = 0):
    # Find the next open square in the grid.
    i, j = findNext(grid, i, j)
    
    # If there are no open squares the puzzle is solved :).
    if i == -1: 
        return True

    for n in range(1, 10):
        if isValid(grid, i, j, n):
            grid[i][j] = n
            #  If solving the new grid returns True,
            #  the solution is complete. Otherwise,
            #  backtrack by setting the current cell to 0.
            if solve(grid, i, j):
                return True
            else:
                grid[i][j] = 0
    
    #  If none of the 10 values work for that cell, return
    #  False to backtrack.
    return False


def findNext(grid, i, j):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    
    return -1, -1


def isValid(grid, i, j, n):
    
    # Checks that the current row does not have the value n in it already.
    check_row = all(n != grid[i][y] for y in range(9))
    if not check_row:
        return False

    # Checks that the current col does not have the value n in it already.
    check_col = all(n != grid[x][j] for x in range(9))
    if not check_col:
        return False

    # Checks that the current box does not have the value n in it already.
    box_x, box_y = 3 * (i // 3), 3 * (j // 3)
    for x in range(box_x, box_x + 3):
        for y in range(box_y, box_y + 3):
            if grid[x][y] == n:
                return False
    
    return True

def print_solution(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(f'{grid[i][j]} ', end="") 


if __name__ == "__main__":
    input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
    print(solve(input))
    print_solution(input)
