import os

def fold_board(board, axis, line):
    if axis == 'x':
        base_board = [row[:line] for row in board]
        second_board = [row[line+1:][::-1] for row in board]
    if axis == 'y':
        base_board = board[:line]
        second_board = board[:line:-1]
        temp = []

    for row_index in range(len(second_board)):
        for col_index in range(len(second_board[0])):
            if second_board[row_index][col_index] == "░":
                base_board[row_index][col_index] = '░'

    return base_board

if __name__ == "__main__":
    # Create board
    folds = []
    spots = []
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        line_count = sum(1 for line in f)
        f.seek(0)
        for i in range(line_count):
            line = f.readline()
            if line.startswith("fold along"):
                folds.append(line.strip()[11:].split('='))
            elif line != '\n':
                spots.append(list(map(int, line.strip().split(','))))

    max_x = max([x[0] for x in spots])
    max_y = max([x[1] for x in spots])

    print(folds)

    board = [[" " for __ in range(max_x + 1)] for _ in range(max_y + 1)]
    for spot in spots:
        board[spot[1]][spot[0]] = "░"

    # Fold board
    for i in range(len(folds)):
        board = fold_board(board, folds[i][0], int(folds[i][1]))
    for row in board:
        print(''.join(row))