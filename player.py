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
