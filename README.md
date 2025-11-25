Python Checkers Game (CLI)

This is a command-line interface (CLI) implementation of the classic **Checkers** game (also known as Draughts) using Python.

The game is played on an 8x8 board, and it includes logic for standard moves, jumps (captures), kinging, and multi-jump sequences.


Prerequisites

This script requires a standard Python 3 environment. It uses the `copy` module for deep copying the board state (though `copy` isn't actively used in the provided code, it's imported, suggesting potential future use in AI or move simulation).

No external libraries are required.


No special installation needed, just a standard Python interpreter



How to Play

1.  Save the Code: Save the provided Python code as a file (e.g., checkers.py).

2.  Run from Terminal: Execute the script from your command line:

    
    python checkers.py
    

3.  Gameplay:

       The game starts with Player X (the pieces on rows 5-7, moving up) going first.
       The board and current player are displayed.
       When prompted, enter your move using four numbers separated by spaces: from_row from_col to_row to_col.

    Example Move (Moving from row 5, column 0 to row 4, column 1):


    Enter move (from_row from_col to_row to_col): 5 0 4 1

4.  Multi-Jumps: If you make a jump (a capture) and can jump again from the new position, the game will prompt you to make the next jump move immediately without changing the turn.



Game Rules Implemented

Feature And Description And Pieces 

Players  'X' starts at the bottom, moves up. 'O' starts at the top, moves down.  X (Player 1) and O (Player 2). 
Movement  Standard pieces can only move one step diagonally forward (towards the opponent's side). 
Jumping (Capture)  Pieces must jump over an adjacent opponent's piece into an empty square two steps away. The jumped piece is removed. 
Kinging  When a player's piece reaches the opponent's back row (row 0 for 'X', row 7 for 'O'). KX (King X) and KO (King O). 
King Movement  Kings can move and jump diagonally in both forward and backward directions. 
Forced Jumps  The logic for calculating valid moves prioritizes jumps. If any jump is possible, only jump moves will be accepted. 



Code Structure Overview

Function And Purpose 
initialize_board() -- Sets up the initial 8x8 checkers board with 'X' and 'O' pieces. 
display_board(board) -- Prints the current state of the board to the console, including row and column indices. 
is_valid_position(r, c) -- Checks if a given row and column are within the $8 \times 8$ board boundaries. 
is_valid_move(...) -- Determines if a move (single step or jump) is legal for the specified player and piece. 
make_move(...) -- Executes a move, updating the board, removing jumped pieces, and checking for King promotion. 
can_jump(...) -- Checks if a specific piece at (row, col) can make any jump move. 
get_possible_moves(...) -- Returns a list of all legal moves (prioritizing jumps) for the current player. 
is_game_over(...) -- Checks if the current player has lost all their pieces or has no legal moves remaining. 
play_checkers() -- The main game loop function that handles player turns, input, move validation, and game termination. 



Next Steps

Implement AI:The current structure makes it easy to add an AI player (e.g., using the Minimax algorithm) by utilizing the `get_possible_moves` and `make_move` functions to simulate future board states.
GUI: Wrap the core game logic with a graphical interface using libraries like Tkinter or Pygame.
