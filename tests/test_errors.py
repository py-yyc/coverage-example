import ttt


def test_invalid_wrong_size():
    board = [
        'x', '.', 'o',
    ]
    assert ttt.GameStates.invalid == ttt.game_state(board)


def test_invalid_illegal_char():
    board = [
        'x', '.', 'o',
        'x', '.', 'o',
        'x', '.', 'O',
    ]
    assert ttt.GameStates.invalid == ttt.game_state(board)


def test_invalid_too_many_o_moves():
    board = [
        'x', '.', 'o',
        'x', '.', 'o',
        'x', 'o', 'o',
    ]
    assert ttt.GameStates.invalid == ttt.game_state(board)


def test_invalid_two_winners():
    board = [
        'o', 'x', '.',
        'o', 'x', '.',
        'o', 'x', '.',
    ]
    assert ttt.GameStates.invalid == ttt.game_state(board)


def test_incomplete_0():
    board = [
        'x', 'x', 'o',
        'o', 'x', 'o',
        'x', 'o', '.',
    ]
    assert ttt.GameStates.unfinished == ttt.game_state(board)


def test_draw():
    board = [
        'x', 'x', 'o',
        'o', 'x', 'x',
        'x', 'o', 'o',
    ]
    assert ttt.GameStates.draw == ttt.game_state(board)
