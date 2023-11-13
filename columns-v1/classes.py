from typing import List

class Square:
    def __init__(self, *, height: int, width: int, id: str):
        self.height = height
        self.width = width
        self.id = id

    def calculate_surface_area(self):
        return self.height * self.width


class Column:
    def __init__(self, *, squares: List[Square]):
        self.squares = squares
        self.height = sum(square.height for square in self.squares)
        self.width = max(square.width for square in self.squares)


class SquareWithVariants:
    def __init__(self, *, squares: List[Square]):
        self.squares = squares

    def get(self, index: int) -> Square:
        return self.squares[index - 1]
