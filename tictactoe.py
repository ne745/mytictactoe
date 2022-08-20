from player import RandomPlayer, BetterPlayer, BestPlayer


MARKS = {0: 'X', 1: 'O'}


class Board:
    def __init__(self):
        self.state = [None] * 9
        self.counter = 0

    def render(self):
        text = '0|1|2\n'
        text += '-----\n'
        text += '3|4|5\n'
        text += '-----\n'
        text += '6|7|8\n'

        for idx, x in enumerate(self.state):
            if x is not None:
                text = text.replace(str(idx), MARKS[x])

        print(text)

    def move(self, idx):
        if self.state[idx] is not None:
            return False

        self.state[idx] = self.counter % 2
        self.counter += 1
        return True

    def unmove(self, idx):
        self.state[idx] = None
        self.counter -= 1
        return True

    def is_win(self, player):
        s = self.state
        return (
            s[0] == s[1] == s[2] == player or
            s[3] == s[4] == s[5] == player or
            s[6] == s[7] == s[8] == player or
            s[0] == s[3] == s[6] == player or
            s[1] == s[4] == s[7] == player or
            s[2] == s[5] == s[8] == player or
            s[0] == s[4] == s[8] == player or
            s[2] == s[4] == s[6] == player
        )

    def is_end(self):
        return self.counter == 9

    def valid_moves(self):
        moves = []
        for idx, player in enumerate(self.state):
            if player is None:
                moves.append(idx)
        return moves


def main():
    board = Board()
    players = [RandomPlayer(), BestPlayer(1)]
    player = 0  # 0 or 1

    while True:
        p = players[player]
        p.play(board)
        board.render()

        if board.is_win(player):
            print(MARKS[player] + ' の勝ち')
            break
        elif board.is_end():
            print('引き分け')
            break
        player = 1 if player == 0 else 0


if __name__ == '__main__':
    main()
