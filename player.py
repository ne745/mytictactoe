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


class BestPlayer(Player):

    def play(self, board):
        score, idx = self._minimax(board, self.player)
        print('最強のAI: ', idx)
        board.move(idx)

    def _minimax(self, board, player):
        """
        ミニマックスアルゴリズム

        Args:
            board(list): 盤面のリスト
            player(int): プレイヤー

        Returns:
            tuple: (スコア, 選択する盤面)
        """

        maximize_player = 0
        minimize_player = 1

        if board.is_win(maximize_player):
            return (1, None)
        elif board.is_win(minimize_player):
            return (-1, None)
        elif board.is_end():
            return (0, None)

        opp = 1 if player == 0 else 0
        if player == maximize_player:
            max_score = -np.inf
            max_idx = None

            for idx in board.valid_moves():
                board.move(idx)
                score, next_idx = self._minimax(board, opp)
                if max_score < score:
                    max_score = score
                    max_idx = idx
                board.unmove(idx)

            return (max_score, max_idx)
        else:
            min_score = np.inf
            min_idx = None

            for idx in board.valid_moves():
                board.move(idx)
                score, next_idx = self._minimax(board, opp)
                if min_score > score:
                    min_score = score
                    min_idx = idx
                board.unmove(idx)

            return (min_score, min_idx)
