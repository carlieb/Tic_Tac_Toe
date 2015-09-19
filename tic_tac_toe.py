def create_board(squares):
  print(squares[1] + '|' + squares[2] + '|' + squares[3])
  print('_____')
  print(squares[4] + '|' + squares[5] + '|' + squares[6])
  print('_____')
  print(squares[7] + '|' + squares[8] + '|' + squares[9])
  print('\n\n\n')
  #\n adds new, blank lines to seperate boards

squares = [' '] * 10

# use 10, instead of 9 (9 squares on the board) so that the first square is not labeld 0--only a matter of preference

def print_intro():
  print('Ciao! Come stai?')
  print('Player 1 is "X"')
  print('Player 2 is "O"')
  print('It\'s your move, Player 1. Typer numbers 1-9 to occupy that square.')
  print('\n\n')
  create_board(squares)
  print(': ')

def record_moves():
  move = 10
  while move not in range(1,10) or is_square_occupied(move):
    move = eval(input('Enter valid move: '))
  squares[move] = 'X'

def is_square_occupied(num):
  if squares[num] == ' ':
    return squares[num] != ' '

print(record_moves())
create_board(squares)
