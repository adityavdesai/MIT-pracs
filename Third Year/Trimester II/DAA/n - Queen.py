allQueensPlaced = False

'''
Checked in 4 steps:
    No Q in same Row
    No Q in same Column
    No Q in same Diagonal (Left Top - Right Bottom)
    No Q in same Diagonal (Right Top - Left Bottom)
'''
def isSafe(result, row, col):
    global n
    if 1 in result[row] or 1 in map(lambda x: x[col], result[:row]) or \
            1 in map(lambda x: result[x[0]][x[1]], zip(range(row - 1, -1, -1), range(col - 1, -1, -1))) or \
            1 in map(lambda x: result[x[0]][x[1]], zip(range(row - 1, -1, -1), range(col + 1, n))):
        return False
    return True



# Add the Q to the solution based on whether it is safe or not
def solve(row, result):
    global n
    for col in range(n):
        if isSafe(result, row, col):
            result[row][col] = 1
            if row + 1 < n:
                if solve(row + 1, result):
                    return True
                result[row][col] = 0
            else:
                return True
    return False


# Initial function do solve the nQueens problem
def nQueens(result):
    if solve(0, result):
        return result


if __name__ == "__main__":
    n = int(input("Enter the size of the chess board (N) :  "))
    result = [[0 for _ in range(n)] for _ in range(n)]
    print(*nQueens(result), sep="\n")
