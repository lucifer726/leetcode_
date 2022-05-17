def searchMatrix(matrix, target):
    m, n = 0, len(matrix[0])-1
    while n >= 0 and m <= len(matrix)-1:
        if matrix[m][n] == target:
            return True
        elif matrix[m][n] > target:
            n -= 1
        else:
            m += 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))