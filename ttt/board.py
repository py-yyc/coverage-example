"""
TicTacToe

x goes first
board is a list of 9 elements from ['x','o','.']. '.' means empty spot.
"""


class GameStates(object):
    """
    Enumeration of the possible games states
    """
    invalid = 0
    unfinished = 1
    x_wins = 2
    o_wins = 3
    draw = 4


def x_count(board):
    """
    count how many 'x'-es are on the board
    """
    return len([ch for ch in board if ch == 'x'])


def o_count(board):
    """
    count how many 'o'-es are on the board
    """
    return len([ch for ch in board if ch == 'o'])


def vertical_win(board, who):
    """
    returns true if there are any vertical winning columns
    """
    for col in range(3):
        num = 0
        for row in range(3):
            if board[row * 3 + col] == who:
                num += 1
        if num == 3:
            return True
    return False


def diagonal_win(board, who):
    """
    returns true if either diagonal contains a winner
    """
    if board[0] == who and board[4] == who and board[8] == who:
        return True
    if board[2] == who and board[4] == who and board[6] == who:
        return True

    return False


def is_winner(board, who):
    """
    returns True of there is a winner

    :param board: the board state

    :param who: an 'x' or 'o', for whom we should check for a winner
    """
    # x, o wins cases (8 cases)
    xt = [who, who, who]
    if board[:3] == xt or board[3:6] == xt or board[6:] == xt:
        return True
    if vertical_win(board, who):
        return True
    if diagonal_win(board, who):
        return True
    return False


def game_state(board):
    """
    determine the current state of the board

    :param board: the board

    :returns: one of the values in GameStates
    """
    # all invalid boards
    if len(board) != 9:
        return GameStates.invalid
    for c in board:
        if c not in ('x', 'o', '.'):
            return GameStates.invalid
    # x goes first, so there's either the same number of x's and o's,
    # or one more x than o
    diff = x_count(board) - o_count(board)
    if diff not in (0, 1):
        return GameStates.invalid

    # x or o winning cases
    if is_winner(board, 'x') and is_winner(board, 'o'):
        return GameStates.invalid
    if is_winner(board, 'x'):
        return GameStates.x_wins
    if is_winner(board, 'o'):
        return GameStates.o_wins

    # draw case (basically: board has no empty spaces, and we haven't
    # detected a winner yet
    if '.' not in board:
        return GameStates.draw

    # everything else is just incomplete
    return GameStates.unfinished
