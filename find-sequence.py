def checkio(matrix):
    #replace this for solution
    #print(len(matrix))
    for y in range(len(matrix)-3):
        for x in range(len(matrix)-3):
            for j in range(len(matrix)):
                flagy = (0 if y+j<len(matrix) else 2*y+j)
                flagx = (0 if x+j<len(matrix) else 2*x+j)
                if matrix[y+j-flagy][x] == matrix[y+j-flagy][x+1] == matrix[y+j-flagy][x+2] == matrix[y+j-flagy][x+3]:
                    return True
                if matrix[y][x+j-flagx] == matrix[y+1][x+j-flagx] == matrix[y+2][x+j-flagx] == matrix[y+3][x+j-flagx]:
                    return True
            if matrix[y][x] == matrix[y+1][x+1] == matrix[y+2][x+2] == matrix[y+3][x+3]:
                return True
            if matrix[y][x+3] == matrix[y+1][x+2] == matrix[y+2][x+1] == matrix[y+3][x]:
                return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # print( checkio([
    #     [1, 2, 1, 1],
    #     [1, 1, 4, 1],
    #     [1, 3, 1, 6],
    #     [1, 7, 2, 5]
    # ]))# == True, "Vertical"
    # print( checkio([
    #     [7, 1, 4, 1],
    #     [1, 2, 5, 2],
    #     [3, 4, 1, 3],
    #     [1, 1, 8, 1]
    # ]))# == False, "Nothing here"
    # print( checkio([
    #     [2, 1, 1, 6, 1],
    #     [1, 3, 2, 1, 1],
    #     [4, 1, 1, 3, 1],
    #     [5, 5, 5, 5, 5],
    #     [1, 1, 3, 1, 1]
    # ]))# == True, "Long Horizontal"
    print( checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]))# == True, "Diagonal"
    # print(checkio([
    #     [6, 9, 1, 1, 6, 2],
    #     [5, 9, 7, 8, 2, 5],
    #     [2, 1, 1, 7, 9, 8],
    #     [1, 8, 1, 4, 7, 4],
    #     [7, 8, 5, 4, 5, 1],
    #     [6, 4, 8, 8, 1, 8]]))
