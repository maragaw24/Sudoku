
#Backtracking algorithm, implemented recursively
def solve(bo):
    find = find_empty(bo) #retrieve an empty space on board
    if not find: #if there are no empty spaces, return true to end
        return True #defining our base case of our recursive algorithm
    else: #if there is an empty space
        row, col = find #assign row and col to the coordinates of it
    for i in range(1,10): #attempt every value 1 through 9 into board
        if valid(bo, i, (row, col)): #if the number being attempted in the loop is valid ...
            bo[row][col] = i #then add the value into the board
            if solve(bo): #call solve again, with this new value added
                return True
            bo[row][col] = 0
        #once we get to the point that we have looped through all the numbers and none are valid, solve returns false,
        #so then the if statement with the new value added is no longer called, and moves to the next line
        #where the originally inserted value is reset to zero, then the process is tried again
    return False

#return bool, false if not valid in space, checks if a number is valid in a given position
def valid(bo, num, pos):
    #we need to check the row, the column, and the 3x3 grid
    #check row:
    for i in range(len(bo[0])):
    # pos[0] because i must iterate through the row to check if the number added in already exists in the row, \
    # and second condition makes sure we arent checking the just inserted element (will be done in an insert function)
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 grids
    #first, determine which grid we are in, using integer division
    # mapping the boxes as a (0,2) coordinate system
    box_x = pos[1] // 3
    box_y = pos[0] // 3 #floor(integer) division

    for i in range(box_y*3, box_y*3 + 3): #multiplying what box you are in by 3 will give you the index values, so you can use it in board array
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

#print the given board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0: #
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8: #once you get to end of the row, moves next row
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#find an empty square on the board
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #returns location of empty space as a two element array, the row and the column
    return None
