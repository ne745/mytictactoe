import numpy as np


class RandomPlayer:
    def play(self, board):
        moves = board.valid_moves()
        idx = np.random.choice(moves)
        print('ランダムプレイヤー: ', idx)
        board.move(idx)
