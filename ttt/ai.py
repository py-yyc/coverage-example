
import abc


class IPlayer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def next_move(self, board):
        """
        return a new next move (as a 2-tuple) given a particular board
        """


def create_ai_for(player):
    """
    Create and return a new object implementing IPlayer

    :param player: 'x' or 'o' to indicate which player we are
    """
    return DeepTicTac(player)


class DeepTicTac(object):
    """
    An advanced TicTacToe intelligence
    """

    def __init__(self, me='x'):
        if me not in ('x', 'o'):
            raise ValueError(
                "me= must be 'x' or 'o'"
            )
        self._me = me

    def next_move(self, board):
        """
        return a new next move (as a 2-tuple) given a particular board
        """
        # for now, return the first available valid move
        for x in range(3):
            for y in range(3):
                if board[y * 3 + x] == '.':
                    return (x, y)


IPlayer.register(DeepTicTac)
