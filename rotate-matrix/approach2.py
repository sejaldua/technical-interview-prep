def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :return type: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])    
        
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
    
    # reverse each row
    for i in range(n):
        matrix[i].reverse()

    print(matrix)

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

rotate(mat)