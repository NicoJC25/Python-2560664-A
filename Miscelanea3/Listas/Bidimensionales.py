EMPTY = "-"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print('Mostrar todos los elementos de la matriz fila por fila')
for row in matrix:
    print(row)

print('Mostrar todos los elementos de la matriz elemento a elemento en columna')
for row in matrix:
    for element in row:
        print(element)

print('Mostrar todos los elementos de una matriz en formato de matriz')
for row in matrix:
    for wlwment in row:
        print(element, end=' ')
    print()