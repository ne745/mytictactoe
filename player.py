from abc import ABC, abstractmethod

import numpy as np


class Player(ABC):

    def __init__(self, player=None):
        self.player = player

    @abstractmethod
    def play(self, board):
        pass


class RandomPlayer(Player):

    def play(self, board):
        moves = board.valid_moves()
        idx = np.random.choice(moves)
        print('ランダムプレイヤー: ', idx)
        board.move(idx)


class BetterPlayer(Player):

    def play(self, board):
        moves = board.valid_moves()

        for idx in moves:
            board.move(idx)
            if board.is_win(self.player):
                print('少し賢いプレイヤー: ', idx)
                return
            board.unmove(idx)

        idx = np.random.choice(moves)
        print('少し賢いプレイヤー: ', idx)
        board.move(idx)
