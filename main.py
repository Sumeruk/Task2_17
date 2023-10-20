def readfile():
    with open('input.txt', 'r') as file:
        lst = file.readlines()
    lst = [[float(n) for n in x.split()] for x in lst]
    return lst


def write(array):
    with open('output.txt', 'w') as testfile:
        for row in array:
            testfile.write(' '.join([str(a) for a in row]) + '\n')


def isMatrixSquare(array):
    for i in range(len(array)):
        if len(array) != len(array[i]):
            return False


def solution(array):
    a = len(array)
    res = [[False] * a for _ in range(a)]
    arrRow = [[False] * a for _ in range(a)]
    arrCol = [[False] * a for _ in range(a)]

    if isMatrixSquare(array) is False:
        return 'null'

    for i in range(len(array)):
        minElement = array[i][0]

        for j in range(len(array[i])):
            if array[i][j] < minElement:
                minElement = array[i][j]

        for j in range(len(array[i])):
            if minElement == array[i][j]:
                arrRow[i][j] = True
                break

    for j in range(len(array[0])):
        maxElement = array[0][j]

        for i in range(len(array)):
            if array[i][j] > maxElement:
                maxElement = array[i][j]

        for i in range(len(array)):

            if maxElement == array[i][j]:
                arrCol[i][j] = True
                break

    for i in range(len(array)):
        for j in range(len(array)):
            if arrCol[i][j] is True and arrRow[i][j] is True:
                res[i][j] = True
    return res


arr = readfile()
write(solution(arr))
