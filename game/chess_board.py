class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p"] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            ["P"] * 8,
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
        return board

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
