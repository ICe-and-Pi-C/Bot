# Определитель матрицы - determinant

def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        sum = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            sum += mul * determinant(m, sign * matrix[0][i])
        return round(sum)

def parse_matrix(s):
    a = s.split("\\\\\\\\")
    for i in range(len(a)):
        a[i] = a[i].split('&')
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = int(a[i][j])
    return a

