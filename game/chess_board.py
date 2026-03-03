import pygame


class BoardSquare:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 64,
        height: int = 64,
        row: int = 0,
        col: int = 0,
        color: str = "white",
        piece=None,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.row = row
        self.col = col
        self.piece = piece

    def is_occupied(self):
        return self.piece is not None

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def draw(self, screen):
        pygame.draw.rect(
            surface=screen,
            color=self.color,
            rect=pygame.Rect(self.x, self.y, self.width, self.height),
        )

    def __str__(self):
        return f"BoardSquare(row={self.row}, col={self.col}, color={self.color}, piece={self.piece})"


class ChessBoard:
    def __init__(self):
        self.board: list[BoardSquare] = []
        self.create_board()

    def create_board(self):
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "grey16"
                square = BoardSquare(
                    x=i * 64 + 32,
                    y=j * 64 + 32,
                    row=i,
                    col=j,
                    color=color,
                )
                self.board.append(square)

    def display_board(self, screen):
        pygame.draw.rect(
            surface=screen,
            color="white",
            rect=pygame.Rect(30, 30, 516, 516),
        )

        for row in self.board:
            row.draw(screen)
