def mark_cell(current_row, current_col):
    if 0 < current_row > rows - 1 or 0 < current_col > cols - 1:
        return

    if mapData[current_row][current_col] == '.':
        mapData[current_row][current_col] = 'x'
        return


def dispose(current_row, current_col):
    mark_cell(current_row - 1, current_col)
    mark_cell(current_row + 1, current_col)
    mark_cell(current_row, current_col - 1)
    mark_cell(current_row, current_col + 1)
    return


if __name__ == '__main__':
    with open('standard_input.txt', 'r') as file:
        inputData = file.read().split('\n')

    mapSize = tuple(map(int, inputData[0].split()))
    rows = mapSize[0]
    cols = mapSize[1]

    mapData = [list(s) for s in inputData[1::]]

    for row in range(rows):
        for col in range(cols):
            if mapData[row][col] == '0':
                dispose(row, col)

    days = sum(x.count('.') for x in mapData)

    with open('standard_output.txt', 'w') as file:
        file.write(str(days))
