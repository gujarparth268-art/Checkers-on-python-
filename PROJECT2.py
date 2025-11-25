import copy


BOARD_SIZE = 8


def initialize_board():
    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:  
                if row < 3:
                    board[row][col] = 'O'  
                elif row > 4:
                    board[row][col] = 'X'  
    return board


def display_board(board):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print()


def is_valid_position(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


def is_valid_move(board, player, start_row, start_col, end_row, end_col):
    if not is_valid_position(start_row, start_col) or not is_valid_position(end_row, end_col):
        return False
    piece = board[start_row][start_col]
    if piece.lower() != player.lower():
        return False
    if board[end_row][end_col] != ' ':
        return False
    
    row_diff = end_row - start_row
    col_diff = end_col - start_col
    
    
    if abs(row_diff) == 1 and abs(col_diff) == 1:
        if piece.isupper():  
            return True
        elif player == 'X' and row_diff == -1:  
            return True
        elif player == 'O' and row_diff == 1:  
            return True
    
    elif abs(row_diff) == 2 and abs(col_diff) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        mid_piece = board[mid_row][mid_col]
        if mid_piece != ' ' and mid_piece.lower() != player.lower():
            return True
    return False


def make_move(board, start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    board[end_row][end_col] = piece
    board[start_row][start_col] = ' '
    
    
    if abs(end_row - start_row) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        board[mid_row][mid_col] = ' '
    
    
    if piece == 'X' and end_row == 0:
        board[end_row][end_col] = 'KX'
    elif piece == 'O' and end_row == BOARD_SIZE - 1:
        board[end_row][end_col] = 'KO'
    elif piece == 'KX' or piece == 'KO':
        board[end_row][end_col] = piece  


def can_jump(board, row, col, player):
    piece = board[row][col]
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    if not piece.isupper():  
        if player == 'X':
            directions = [(-2, -2), (-2, 2)]
        elif player == 'O':
            directions = [(2, -2), (2, 2)]
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        mr, mc = row + dr // 2, col + dc // 2
        if is_valid_position(nr, nc) and board[nr][nc] == ' ' and board[mr][mc] != ' ' and board[mr][mc].lower() != player.lower():
            return True
    return False


def get_possible_moves(board, player):
    moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col].lower() == player.lower():
                
                if can_jump(board, row, col, player):
                    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
                    if not board[row][col].isupper():
                        if player == 'X':
                            directions = [(-2, -2), (-2, 2)]
                        elif player == 'O':
                            directions = [(2, -2), (2, 2)]
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        mr, mc = row + dr // 2, col + dc // 2
                        if is_valid_position(nr, nc) and board[nr][nc] == ' ' and board[mr][mc] != ' ' and board[mr][mc].lower() != player.lower():
                            moves.append((row, col, nr, nc))
                else:
                    
                    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                    if not board[row][col].isupper():
                        if player == 'X':
                            directions = [(-1, -1), (-1, 1)]
                        elif player == 'O':
                            directions = [(1, -1), (1, 1)]
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if is_valid_position(nr, nc) and board[nr][nc] == ' ':
                            moves.append((row, col, nr, nc))
    return moves


def is_game_over(board, player):
    pieces = sum(1 for row in board for cell in row if cell.lower() == player.lower())
    if pieces == 0:
        return True
    moves = get_possible_moves(board, player)
    return len(moves) == 0


def play_checkers():
    board = initialize_board()
    current_player = 'X'  
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")
        moves = get_possible_moves(board, current_player)
        if not moves:
            print(f"Player {current_player} has no moves. Game over!")
            winner = 'O' if current_player == 'X' else 'X'
            print(f"Player {winner} wins!")
            break
        
        
        while True:
            try:
                move_input = input("Enter move (from_row from_col to_row to_col): ").split()
                if len(move_input) != 4:
                    raise ValueError
                start_row, start_col, end_row, end_col = map(int, move_input)
                if (start_row, start_col, end_row, end_col) in moves:
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter four numbers separated by spaces.")
        
        
        make_move(board, start_row, start_col, end_row, end_col)
        
        
        if abs(end_row - start_row) == 2 and can_jump(board, end_row, end_col, current_player):
            print("You can jump again!")
            continue  
        
        
        current_player = 'O' if current_player == 'X' else 'X'
        
        
        if is_game_over(board, current_player):
            display_board(board)
            print(f"Player {current_player} has no moves or pieces. Game over!")
            winner = 'O' if current_player == 'X' else 'X'
            print(f"Player {winner} wins!")
            break

if __name__ == "__main__":
    play_checkers()
