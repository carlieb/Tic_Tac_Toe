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

def squares_are_full():
  for index in range(1, 10):
    #have to use index in range in order to avoid testing 0, as there is no box assigned to number 0, the loop will always find 0 empty and not test boxes 1-9 which are the real boxes
    if squares[index] == ' ':
      return False
  return True

def three_in_a_row():
  return((squares[1] == squares[2] == squares[3] and squares[1] != ' ') or
    (squares[4] == squares[5] == squares[6] and squares [4] != ' ') or
    (squares[7] == squares[8] == squares[9] and squares [7] != ' ') or
    (squares[1] == squares[4] == squares[7] and squares [1] != ' ') or
    (squares[2] == squares[5] == squares[8] and squares [2] != ' ') or
    (squares[3] == squares[6] == squares[9] and squares [3] != ' ') or
    (squares[1] == squares[5] == squares[9] and squares [1] != ' ') or
    (squares[3] == squares[5] == squares[7] and squares [3] != ' '))

# print(record_moves())
# create_board(squares)
