def create_array(i, j):
    array = [[0] * (j + 1) for _ in range(i + 1)]
    for x in range(i + 1):
        for y in range(j + 1):
            if x > 0 and y == 0:
                array[x][y] = 0
            elif x == 0 and y > 0:
                array[x][y] = 1
            elif x > 0 and y > 0:
                array[x][y] = round((array[x - 1][y] + array[x][y - 1]) / 2, 3)

    return array
n = 5
i = 5
j = 5
result = create_array(i, j)
for row in result:
    print([round(val, 2) for val in row])